import glob

target_grid = """        <div class="student-details-grid">
          <div class="detail-item">
            <span class="detail-icon">🎓</span>
            <div class="detail-text">
              <span class="detail-label">Degree & Program</span>
              <span class="detail-value">B.Tech in Information Technology</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">💻</span>
            <div class="detail-text">
              <span class="detail-label">Laboratory Course</span>
              <span class="detail-value">Advanced Java Programming Lab</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">📋</span>
            <div class="detail-text">
              <span class="detail-label">Course Code</span>
              <span class="detail-value">24IT385</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">🗓️</span>
            <div class="detail-text">
              <span class="detail-label">Academic Year</span>
              <span class="detail-value">2026 – 2027</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">🏛️</span>
            <div class="detail-text">
              <span class="detail-label">Department</span>
              <span class="detail-value">Information Technology (SAHE)</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">📍</span>
            <div class="detail-text">
              <span class="detail-label">Laboratory Venue</span>
              <span class="detail-value">Advanced Java & Enterprise Computing Lab</span>
            </div>
          </div>
        </div>"""

replacement_grid = """        <div class="student-details-grid">
          <div class="detail-item">
            <span class="detail-icon">🎓</span>
            <div class="detail-text">
              <span class="detail-label">Degree & Program</span>
              <span class="detail-value">B.Tech in Information Technology</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">💻</span>
            <div class="detail-text">
              <span class="detail-label">Laboratory Course</span>
              <span class="detail-value">Advanced Java Programming Lab</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">📋</span>
            <div class="detail-text">
              <span class="detail-label">Course Code</span>
              <span class="detail-value">24IT385</span>
            </div>
          </div>
          <div class="detail-item">
            <span class="detail-icon">🗓️</span>
            <div class="detail-text">
              <span class="detail-label">Academic Year</span>
              <span class="detail-value">2026 – 2027</span>
            </div>
          </div>
          <div class="detail-item detail-full-width">
            <span class="detail-icon">🏛️</span>
            <div class="detail-text">
              <span class="detail-label">Department & Institution</span>
              <span class="detail-value">Department of Information Technology · Siddhartha Academy of Higher Education</span>
            </div>
          </div>
        </div>"""

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    c = f.read()

if target_grid in c:
    c = c.replace(target_grid, replacement_grid)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated index.html successfully!")
else:
    print("target_grid not found exactly in index.html, checking whitespace variations")

# 2. Update pages/*.html
for fpath in sorted(glob.glob("pages/*.html")):
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    if target_grid in c:
        c = c.replace(target_grid, replacement_grid)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fpath}")
    else:
        # Check if venue is in file
        if "Laboratory Venue" in c:
            print(f"Warning: 'Laboratory Venue' found in {fpath} but target_grid didn't match exact indentation")

