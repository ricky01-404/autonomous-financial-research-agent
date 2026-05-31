import json
import os


EPISODE_FILE = "data/episodic_memory.json"


class EpisodicMemory:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(EPISODE_FILE):

            with open(EPISODE_FILE, "w") as f:
                json.dump([], f)

    def save_episode(self, episode):

        with open(EPISODE_FILE, "r") as f:

            data = json.load(f)

        data.append(episode)

        with open(EPISODE_FILE, "w") as f:

            json.dump(data, f, indent=4)

    def load_episodes(self):

        with open(EPISODE_FILE, "r") as f:

            return json.load(f)