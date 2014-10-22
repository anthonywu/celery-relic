from pprint import pformat


# === Camera ===

from celery.events.snapshot import Polaroid

class DumpCam(Polaroid):
    """From http://celery.readthedocs.org/en/latest/userguide/monitoring.html#custom-camera"""
    def on_shutter(self, state):
        if not state.event_count:
            # No new events since last snapshot.
            return
        print('Workers: {0}'.format(pformat(state.workers, indent=4)))
        print('Tasks: {0}'.format(pformat(state.tasks, indent=4)))
        print('Total: {0.event_count} events, %s {0.task_count}'.format(state))
