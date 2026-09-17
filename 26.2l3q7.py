threats_db = []

running = True
while running:
    threat_info = input()
    if threat_info == "FIM":
        running = False
    else:
        threat_name, faction, base_damage, intelligence, chaos_factor = (
            threat_info.split(",")
        )

        base_damage = float(base_damage)
        intelligence = int(intelligence)
        chaos_factor = float(chaos_factor)

        initial_level = base_damage + intelligence * chaos_factor
        threat_level = (
            initial_level - (initial_level * 0.15)
            if faction == "Enclave"
            else initial_level
        )
        threat_data = (-threat_level, threat_name, faction)
        threats_db.append(threat_data)

threat_analysis_db = threats_db[:]
factions = [t[2] for t in threat_analysis_db]

for i in range(len(threat_analysis_db)):
    negative_level, threat_name, faction = threat_analysis_db[i]
    positive_level = -negative_level
    faction_frequence = factions.count(faction)
    adjusted_level = positive_level + (positive_level * 0.05 * (faction_frequence - 1))
    threat_analysis_db[i] = (-adjusted_level, threat_name, faction)

threat_analysis_db.sort()

prioritary_area = threat_analysis_db[:3]
# follow_up_area = threat_analysis_db[3:]

print(prioritary_area)
