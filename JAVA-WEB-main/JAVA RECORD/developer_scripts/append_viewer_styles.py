# -*- coding: utf-8 -*-
"""
Appends terminal, code viewer, and button styling to style.css and assets/css/topic-page.css
"""

styles = """
/* ==========================================================================
   PROGRAM CARDS: CODE VIEWER, TERMINAL OUTPUT & ACTIONS (EMERALD THEME)
   ========================================================================== */

.code-editor-block {
  margin: 14px 18px;
  background: #022C22;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
  border: 1px solid #064E3B;
}

.code-viewer-pre {
  margin: 0;
  padding: 16px 20px;
  background: #022C22;
  color: #ECFDF5;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.84rem;
  line-height: 1.6;
  overflow-x: auto;
}

.code-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
  background: rgba(255, 255, 255, 0.12);
  color: #D1FAE5;
  border: 1px solid rgba(209, 250, 229, 0.2);
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.code-action-btn:hover {
  background: #059669;
  color: #FFFFFF;
  border-color: #10B981;
}

.sql-code-viewer {
  margin: 0;
  padding: 14px 18px;
  background: #0F172A;
  color: #38BDF8;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.82rem;
  line-height: 1.55;
  overflow-x: auto;
}

.terminal-output-box {
  background: #0F172A;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 10px;
  border: 1px solid #1E293B;
}

.terminal-bar {
  background: #1E293B;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.terminal-title {
  font-size: 0.72rem;
  font-weight: 600;
  color: #94A3B8;
  letter-spacing: 0.5px;
}

.terminal-text {
  margin: 0;
  padding: 14px 18px;
  color: #4ADE80;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 0.82rem;
  line-height: 1.5;
  white-space: pre-wrap;
  word-break: break-word;
}

.sub-block-heading {
  font-size: 0.88rem;
  font-weight: 700;
  color: #064E3B;
  margin: 12px 0 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}
"""

for target in ["style.css", "assets/css/topic-page.css"]:
    with open(target, "r", encoding="utf-8") as f:
        c = f.read()
    if ".terminal-output-box" not in c:
        with open(target, "a", encoding="utf-8") as f:
            f.write(styles)
        print(f"Appended terminal & code styles to {target}")
    else:
        print(f"{target} already has terminal styles.")

