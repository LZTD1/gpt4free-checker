from __future__ import annotations
import logging
import g4f
from typing import List, Set
from .models import ProviderReport, Capability
from .config import CONFIG

log = logging.getLogger(__name__)

def _infer_capabilities_from_metadata(provider_cls, model: str) -> Set[Capability]:
    caps = {Capability.TEXT}
    m_lower = model.lower()
    
    if hasattr(provider_cls, "image_models") and provider_cls.image_models:
        if model in provider_cls.image_models:
            caps.add(Capability.IMAGE)
            caps.discard(Capability.TEXT)
            
    if hasattr(provider_cls, "audio_models") and provider_cls.audio_models:
        if model in provider_cls.audio_models:
            caps.add(Capability.AUDIO)
            caps.discard(Capability.TEXT)
            
    if any(k in m_lower for k in ("flux", "dall", "stable-diffusion", "sdxl", "midjourney", "diffusion", "playground")):
        caps.add(Capability.IMAGE)
        caps.discard(Capability.TEXT)
    if any(k in m_lower for k in ("tts", "speech", "whisper", "audio")):
        caps.add(Capability.AUDIO)
        caps.discard(Capability.TEXT)
    if any(k in m_lower for k in ("sora", "cogvideo", "luma", "hunyuan", "mochi", "ltx-video", "wan2.0")):
        caps.add(Capability.VIDEO)
        caps.discard(Capability.TEXT)

    if Capability.IMAGE in caps:
        media_required_keywords = (
            "kontext", "img2img", "inpainting",
            "upscale", "pix2pix"
        )
        if any(k in m_lower for k in media_required_keywords):
            caps.discard(Capability.IMAGE)

    return caps


class Discovery:
    @staticmethod
    def get_providers() -> List[ProviderReport]:
        reports: List[ProviderReport] = []
        
        for provider in g4f.Provider.__providers__:
            name = provider.__name__
            
            if name in ("RetryProvider", "BaseProvider", "AsyncProvider", "AsyncGeneratorProvider"):
                continue
                
            if CONFIG.filter_providers and name not in CONFIG.filter_providers:
                continue
                
            needs_auth = getattr(provider, "needs_auth", False)
            if needs_auth and not CONFIG.include_auth:
                log.debug("Skipping auth-required provider: %s", name)
                continue
                
            models_list = []
            if hasattr(provider, "models") and provider.models:
                models_list = list(provider.models)
            
            seen = set()
            unique_models = []
            for m in models_list:
                if m not in seen:
                    seen.add(m)
                    unique_models.append(m)
                    
            models_meta = []
            for m in unique_models:
                caps = _infer_capabilities_from_metadata(provider, m)
                if CONFIG.filter_capabilities:
                    caps = {c for c in caps if c.value in CONFIG.filter_capabilities}
                if caps:
                    models_meta.append({"id": m, "capabilities": list(caps)})

            report = ProviderReport(
                name=name,
                url=getattr(provider, "url", None),
                label=getattr(provider, "label", name),
                model_count=len(models_meta),
                models_meta=models_meta
            )
            reports.append(report)
            
        return reports