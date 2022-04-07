"""Support for Hekr sensors."""

__all__ = [
    "PLATFORM_SCHEMA",
    "async_setup_platform",
    "async_setup_entry",
    "HekrSensor",
]

import logging
from typing import Optional

from homeassistant.components.sensor import (
    PLATFORM_SCHEMA,
    DOMAIN as PLATFORM_DOMAIN,
    SensorEntity,
    ATTR_STATE_CLASS,
)
from homeassistant.helpers.restore_state import RestoreEntity

from .base_platform import HekrEntity, create_platform_basics

_LOGGER = logging.getLogger(__name__)


class HekrSensor(HekrEntity, RestoreEntity, SensorEntity):
    @property
    def unique_id(self) -> Optional[str]:
        return "_".join((self._device_id, PLATFORM_DOMAIN, self._ent_type))

    @property
    def state_class(self) -> Optional[str]:
        return self._config.get(ATTR_STATE_CLASS)


PLATFORM_SCHEMA, async_setup_platform, async_setup_entry = create_platform_basics(
    logger=_LOGGER,
    entity_domain=PLATFORM_DOMAIN,
    entity_factory=HekrSensor,
    base_schema=PLATFORM_SCHEMA,
)
