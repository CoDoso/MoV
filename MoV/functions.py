import time
import datetime
import main
import yaml
from Game_Values import settings
from Game_Values import commanders as com


def log_error(e_type, location, message, failed_params="None"):
    """Records Custom Error Data for Debugging in an Error Log File.
                Parameters
                -----------
                e_type: :class:`str`
                    Type of Error that has Occurred( / or just Unknown).
                location: :class:`str`
                    The Function / Location this Error was found in.
                message: :class:`str`
                    Extra Custom Data for Debugging.
                failed_params: :class:`list`
                    OPTIONAL: List of Values that caused the Error to Occur.
                """
    with open(f"error_log.yml", 'a') as File:
        yaml.safe_dump({
            f'{datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}': {
                "Type": e_type,
                "location": location,
                "message": message,
                "failed params": failed_params
            }
        }, File, default_flow_style=False, sort_keys=False)


def wait(time_seconds: int, location: str):
    print("Slept in ", location, " function at: ", datetime.datetime.now())
    time.sleep(time_seconds)


def next_daytime_in_hours(location: str):
    print("Checked Day-Cooldown in ", location, " function at: ", datetime.datetime.now())
    now = datetime.datetime.now()
    return ((((now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0) - now).total_seconds()) / 60) / 60


def create_user(name, owner_id, age, Dev_Char, Prio_Char, Diff, Trade):
    """Creates a new User with the given Settings
            Parameters
            -----------
            name: :class:`str`
                The Name of the Character.
            owner_id: :class:`int`
                The Discord ID of the Owners Account.
            age: :class:`str`
                Datetime of Character Creation
            Dev_Char: :class:`bool`
                Is Developer/Debug Character?
            Prio_Char: :class:`bool`
                Is Priority Character
            Diff: :class:`int`
                Character Difficulty Setting
            Trade: :class:`bool`
                Is Trading Allowed: Bool
            """
    with open(f"users.yml", 'r') as prev_File:
        i: int = 0
        try:
            for user in yaml.safe_load(prev_File):
                i += 1
        except TypeError:
            pass
        user_data = {
            i+1: {
                "Character": {
                    "Name": name,
                    "Level": 0,
                    "Gold": 50,
                    "Reputation": 0,
                    "Owner": owner_id,
                    "Alliance": None,
                    "Age": f"{age}",
                    "Skills": {
                        "Combat": 0,  # Higher DMG in both 1v1 and Army Combat.
                        "Exploring": 0,  # Higher Chances of Finding Hero's your looking for.
                        "Looting": 0,  # Better and more Dungeon and Raiding Loot.
                        "Medicine": 0,  # Higher Regen, and better outcome for combat Healing.
                        "Alchemy": 0  # Better Potion brewing results, longer Potion Duration.
                    },
                    "Progression": {
                        "Campaign_Level": 0,
                        "Campaign_Quest": 0,
                        "Tournament_Rank": 0,
                    }
                },
                "Status": {
                    "debug/developer char": Dev_Char,
                    "priority char": Prio_Char,
                    "difficulty": Diff,
                    "allow_trading": Trade,
                },
                "Cooldowns": {
                    "Raids": {
                        "Easy": {"Ireland": 0, "Pomerania": 0, "Baltic": 0},  # 0 = ready, 1 on_cooldown, 2 Locked
                        "Hard": {"England": 2, "Rus": 2, "Lowlands": 2},
                        "Extreme": {"Germany": 2, "Francia": 2},
                        "Ultimate": {"Constantinople": 2},
                    },
                    "Game": {},
                    "Events": {}
                },
                "Combat": {
                    "Global Modifiers": {},
                    "Commanders": {},
                    "Armies": {}
                }
            }
        }
        with open(f"users.yml", 'a') as File:
            yaml.safe_dump(user_data, File, default_flow_style=False, sort_keys=False)
