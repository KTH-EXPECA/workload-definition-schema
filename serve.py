from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from build import build_site
import json
import jsonschema2md

class SchemaBuildEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        try:
            build_site()
        except json.JSONDecodeError:
            pass
        return super().on_any_event(event)

if __name__ == '__main__':
    obs = Observer()
    obs.schedule(SchemaBuildEventHandler(), './schemas', recursive=True)
    obs.start()
    try:
        while obs.is_alive():
            obs.join(1)
    except KeyboardInterrupt:
        obs.stop()
    obs.join()