import glob
import re

modal_template = """
  <!-- STUDENT PROFILE DETAILS MODAL -->
  <div id="studentProfileModal" class="student-modal-overlay" aria-hidden="true" role="dialog" aria-labelledby="studentModalTitle">
    <div class="student-modal-card">
      <button class="student-modal-close" id="studentModalCloseBtn" aria-label="Close Profile Details" title="Close (Esc)">&times;</button>
      <div class="student-modal-header">
        <div class="student-modal-photo-wrap">
          <img src="{photo_path}" alt="Venkata Sai Karthikeya Kaja" class="student-modal-photo" />
          <span class="verified-ribbon">✓ Verified Student</span>
        </div>
        <div class="student-modal-title-area">
          <span class="modal-dept-badge">DEPARTMENT OF INFORMATION TECHNOLOGY</span>
          <h2 id="studentModalTitle" class="student-modal-name">Venkata Sai Karthikeya Kaja</h2>
          <div class="student-modal-roll-highlight">
            <span class="roll-label">Roll Number</span>
            <span class="roll-number">24EU08161</span>
          </div>
          <p class="student-modal-institution">Siddhartha Academy of Higher Education</p>
        </div>
      </div>

      <div class="student-modal-body">
        <div class="student-details-grid">
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
        </div>

        <div class="student-modal-footer">
          <div class="footer-status-pill">
            <span class="pulse-dot"></span>
            <span>Digital Laboratory Record · All 14 Weeks Verified</span>
          </div>
        </div>
      </div>
    </div>
  </div>
"""

pill_replacement = """      <div class="header-student-pill" id="studentProfileTrigger" role="button" tabindex="0" title="Click to view student academic details" aria-haspopup="dialog">
        <div class="student-avatar-wrap">
          <img src="{photo_path}" alt="Venkata Sai Karthikeya Kaja" class="student-avatar-img" />
          <span class="student-status-indicator" title="Active Candidate"></span>
        </div>
        <div class="student-pill-info">
          <span class="student-name">Venkata Sai Karthikeya Kaja <span class="profile-hint">Details</span></span>
          <span class="student-dept">IT · Siddhartha Academy of Higher Education</span>
        </div>
      </div>"""

target_pill = re.compile(r'<div class="header-student-pill">.*?<span class="student-dept">IT · Siddhartha Academy of Higher Education</span>\s*</div>\s*</div>', re.DOTALL)

for fpath in glob.glob("pages/*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    new_pill = pill_replacement.format(photo_path="../assets/images/student_photo.jpg")
    content, count_pill = target_pill.subn(new_pill, content)

    # Insert modal if not already present
    if "id=\"studentProfileModal\"" not in content:
        modal_html = modal_template.format(photo_path="../assets/images/student_photo.jpg")
        if "id=\"zoom-modal\"" in content:
            pos = content.find("</div>", content.find("id=\"zoom-modal\"")) + 6
            # find end of zoom modal
            zoom_end = content.find("</div>\n  </div>", content.find("id=\"zoom-modal\""))
            if zoom_end != -1:
                zoom_end += 16
                content = content[:zoom_end] + "\n" + modal_html + content[zoom_end:]
            else:
                body_pos = content.rfind("</body>")
                content = content[:body_pos] + "\n" + modal_html + content[body_pos:]
        else:
            body_pos = content.rfind("</body>")
            content = content[:body_pos] + "\n" + modal_html + content[body_pos:]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {fpath} (pill replaced: {count_pill})")

print("All pages in pages/ updated successfully.")

