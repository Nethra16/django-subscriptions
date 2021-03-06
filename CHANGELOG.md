# Changelog

## v2.0.0 (2020-04-19)

- Dropped support for Django < 2.2
- Dropped support for Python 2
- Made dependencies >= rather than ^ to support a greater range
- Changed the log messages generated by the celery tasks
- Added the pk of the subscription to the str/repr to aid debugging

## v1.1.0 (2019-10-07)

- Transition methods that received a `reason` argument now accept a `description` argument,
  which is stored on the state log, so that reasons aren't lost. Reason is still valid,
  but will not be persisted to the state log. Migrate to using `description`, and it will
  log in the state log AND the `reason` field.
  `state_unknown`, `renewal_failed`, `end_subscription` are affected.

## v1.0.1 (2019-09-13)

- SubscriptionState.choices is now sorted, so that the order is consistent between python versions,
  and migrations are not generated by applications.

## v1.0.0 (2019-07-03)

- **Breaking Change** `suspended_timeout` now triggers for subscriptions in SUSPENDED state that are
  `timeout_hours` past the `subscription.end` time. It used to trigger if `subscription.last_updated`
  hadn't changed for `timeout_hours`, but if `trigger_suspended` was running daily, the subscription
  was constantly being updated, and `trigger_suspended_timeout` would never find a record to `end()`.


## v0.5.1 (2019-06-13)

- Only localise datetimes to dates when they are aware

## v0.5.0 (2019-06-04)

- Display start/end dates in the local timezone
- Changed the display of Subscription.__str__
- Renewed can now be called from Active state, for an early renewal.

## v0.4.0 (2019-05-07)

- Added a new trigger for renewing subscriptions in SUSPENDED state, which helps for retries
- Changed `timeout_days` to `timeout_hours` in `suspended_timeout`. `timeout_hours` is still around
  for backward compatibility


## v0.3.0 (2019-05-01)

- Generated missing migration file
- Added a migrate.py helper for generating migrations
- Updated version dependencies to (hopefully) make this installable under py2.7

## v0.2.0 (2019-04-13)

- Initial working release
- Subscription models, tasks, and signals defined
