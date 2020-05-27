# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from enum import IntEnum


class SubscriptionState(IntEnum):
    ACTIVE = 1
    EXPIRING = 2
    RENEWING = 3
    SUSPENDED = 4
    ENDED = 5
    TRIAL_SCHEDULED = 6
    TRIAL_ACTIVE = 7
    TRIAL_ENDED = 8
    ERROR = -1

    @classmethod
    def choices(cls):
        return sorted(tuple((s.value, "{}".format(SubscriptionState(s.value).name)) for s in cls))
