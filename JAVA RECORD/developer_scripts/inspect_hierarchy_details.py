import hierarchy_metadata

for w in hierarchy_metadata.HIERARCHY_DATA:
    wnum = w["num"]
    print(f"\n=== WEEK {wnum}: {w['name']} ===")
    for t in w["tasks"]:
        print(f"  Task: {t['id']} - {t['title']}")
        print(f"    Aim: {t['aim'][:60]}...")
        reqs = t.get("requirements", [])
        print(f"    Requirements count: {len(reqs)}")
        progs = t.get("programs", [])
        print(f"    Programs count: {len(progs)}")
        for p in progs:
            has_code = bool(p.get("code"))
            has_sql = bool(p.get("sql_setup"))
            has_expl = bool(p.get("explanation"))
            has_out = bool(p.get("output"))
            print(f"      [{p['id']}] {p['title'][:35]} | Code: {has_code} | SQL: {has_sql} | Expl: {has_expl} | Out: {has_out}")

