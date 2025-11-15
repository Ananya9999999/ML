import fastf1
import os
os.makedirs('cache', exist_ok=True) 
fastf1.Cache.enable_cache('cache') 
session= fastf1.get_session(2024, 'Monaco', 'Qualifying')
session.load()

laps=session.laps.pick_driver('VER')
print(laps['LapTime'].mean())

laps= session.laps.pick_driver('VER')
laps[['LapNumber', 'LapTime', 'Compound', 'Sector1Time', 'Sector2Time', 'Sector3Time']]
print(laps)