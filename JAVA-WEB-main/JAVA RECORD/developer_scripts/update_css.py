# -*- coding: utf-8 -*-
"""
Appends 3-Level Navigation, Program Card, and Profile Dropdown styles
to style.css and assets/css/topic-page.css
"""
import os

css_additions = """
/* ==========================================================================
   3-LEVEL HIERARCHICAL NAVIGATION & PROGRAM CARDS (EMERALD THEME)
   ========================================================================== */

/* Top Navigation Profile Dropdown */
.profile-section {
  position: absolute;
  right: 24px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1001;
}

.profile-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid #10B981;
  overflow: hidden;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  background: #047857;
}

.profile-icon:hover {
  transform: scale(1.08);
  border-color: #34D399;
  box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35);
}

.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.profile-dropdown {
  position: absolute;
  top: 54px;
  right: 0;
  width: 360px;
  background: #FFFFFF;
  border-radius: 12px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.18);
  display: none;
  z-index: 1002;
  border: 1px solid #D1FAE5;
  overflow: hidden;
}

.profile-dropdown.show {
  display: block;
  animation: profileFadeIn 0.2s ease;
}

@keyframes profileFadeIn {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}

.profile-close {
  position: absolute;
  top: 10px;
  right: 12px;
  font-size: 20px;
  font-weight: bold;
  color: #064E3B;
  cursor: pointer;
  z-index: 1003;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 50%;
  width: 26px;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.profile-close:hover {
  background: #FFFFFF;
  color: #DC2626;
}

.profile-header {
  background: linear-gradient(135deg, #059669, #047857);
  color: #FFFFFF;
  padding: 22px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.profile-header-img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: 3px solid #FFFFFF;
  object-fit: cover;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
  flex-shrink: 0;
}

.profile-info h3 {
  margin: 0 0 4px 0;
  font-size: 0.96rem;
  font-weight: 700;
  color: #FFFFFF;
  line-height: 1.2;
}

.profile-info p {
  margin: 0;
  font-size: 0.82rem;
  color: #D1FAE5;
  font-weight: 600;
  letter-spacing: 0.5px;
}

.profile-details {
  padding: 18px 20px;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 8px 0;
  border-bottom: 1px solid #F1F5F9;
  font-size: 0.82rem;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-label {
  font-weight: 600;
  color: #475569;
  min-width: 90px;
}

.detail-value {
  color: #0F172A;
  font-weight: 600;
  text-align: right;
}

/* 3-Level Sidebar Program Navigation */
.sidebar-prog-list {
  display: flex;
  flex-direction: column;
  padding: 2px 0 3px 12px;
  gap: 2px;
  border-left: 1px dashed #CBD5E1;
  margin-left: 6px;
}

.sidebar-prog-link {
  font-size: 0.70rem;
  color: #64748B;
  text-decoration: none;
  padding: 3px 6px;
  border-radius: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  display: flex;
  align-items: center;
  gap: 5px;
  transition: all 0.15s ease;
}

.sidebar-prog-link:hover {
  background: #F1F5F9;
  color: #059669;
}

.sidebar-prog-link.active {
  color: #059669;
  font-weight: 700;
  background: #ECFDF5;
}

.prog-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #94A3B8;
  flex-shrink: 0;
}

.sidebar-prog-link:hover .prog-dot,
.sidebar-prog-link.active .prog-dot {
  background: #10B981;
}

/* Quick-jump In-Page TOC Bar */
.week-toc-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 10px;
  margin-bottom: 24px;
  overflow-x: auto;
  position: sticky;
  top: 70px;
  z-index: 95;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.week-toc-link {
  font-size: 0.74rem;
  font-weight: 600;
  color: #475569;
  text-decoration: none;
  padding: 4px 9px;
  border-radius: 6px;
  background: #F8FAFC;
  white-space: nowrap;
  transition: all 0.15s ease;
  border: 1px solid #E2E8F0;
}

.week-toc-link:hover {
  background: #ECFDF5;
  color: #059669;
  border-color: #A7F3D0;
}

/* Individual Program Cards */
.program-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  margin-bottom: 28px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: box-shadow 0.2s ease, border-color 0.2s ease;
}

.program-card:hover {
  box-shadow: 0 8px 24px rgba(5, 150, 105, 0.08);
  border-color: #A7F3D0;
}

.program-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 18px;
  background: #F8FAFC;
  border-bottom: 1px solid #E2E8F0;
  flex-wrap: wrap;
  gap: 10px;
}

.program-card-title-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.program-badge {
  background: #059669;
  color: #FFFFFF;
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.program-card-title {
  font-size: 0.94rem;
  font-weight: 700;
  color: #0F172A;
  margin: 0;
}

.program-type-tag {
  background: #ECFDF5;
  color: #059669;
  border: 1px solid #A7F3D0;
  padding: 2px 8px;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 600;
}

.program-objective-box {
  padding: 12px 18px;
  background: #F0FDF4;
  border-left: 4px solid #10B981;
  font-size: 0.84rem;
  color: #065F46;
  margin: 14px 18px 0;
  border-radius: 0 8px 8px 0;
}

.program-objective-box strong {
  color: #047857;
}

.program-sql-box {
  margin: 14px 18px;
  background: #0F172A;
  border-radius: 8px;
  overflow: hidden;
}

.sql-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #1E293B;
  padding: 6px 14px;
  color: #94A3B8;
  font-size: 0.72rem;
  font-weight: 600;
}

.program-card-body {
  padding: 14px 18px;
}

/* Program Explanation Table */
.program-explanation-table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 0.82rem;
}

.program-explanation-table th {
  background: #F1F5F9;
  color: #1E293B;
  padding: 9px 12px;
  text-align: left;
  font-weight: 700;
  border: 1px solid #E2E8F0;
}

.program-explanation-table td {
  padding: 8px 12px;
  border: 1px solid #E2E8F0;
  color: #334155;
  line-height: 1.5;
}

.program-explanation-table tr:nth-child(even) td {
  background: #F8FAFC;
}

.program-explanation-table code {
  background: #ECFDF5;
  color: #059669;
  padding: 2px 5px;
  border-radius: 4px;
  font-family: 'Consolas', monospace;
  font-weight: 600;
  font-size: 0.8rem;
}
"""

for target_file in ["style.css", "assets/css/topic-page.css"]:
    if os.path.exists(target_file):
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
        if ".profile-dropdown" not in content:
            with open(target_file, "a", encoding="utf-8") as f:
                f.write(css_additions)
            print(f"Added additions to {target_file}")
        else:
            print(f"{target_file} already has additions.")
