with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace initZoomModal with universal clean lightbox
old_zoom = """/* ─────────────────────────────────────────
   12. CLICK TO ZOOM LIGHTBOX WITH PREV / NEXT & KEYBOARD CYCLING
──────────────────────────────────────────── */
function initZoomModal() {
  const modal = document.getElementById('zoom-modal');
  if (!modal) return;

  const modalImg = modal.querySelector('.modal-img');
  const modalCap = modal.querySelector('.modal-caption');
  const closeBtn = modal.querySelector('.modal-close');
  const prevBtn = modal.querySelector('.modal-prev');
  const nextBtn = modal.querySelector('.modal-next');

  let imagesList = [];
  let currentIndex = 0;

  function updateModalImage(index) {
    if (imagesList.length === 0) return;
    if (index < 0) index = imagesList.length - 1;
    if (index >= imagesList.length) index = 0;
    currentIndex = index;

    const item = imagesList[currentIndex];
    modalImg.src = item.src;
    modalCap.textContent = `${item.caption} (${currentIndex + 1} of ${imagesList.length})`;
  }

  // Find all zoomable images on the page
  function refreshImagesList() {
    imagesList = [];
    document.querySelectorAll('.ss-img-wrap img, .timeline-step-img img').forEach((img, idx) => {
      const card = img.closest('.ss-card, .timeline-card');
      const caption = card ? (card.querySelector('.ss-caption') || card.querySelector('.timeline-title'))?.textContent.trim() : `Figure ${idx + 1}`;
      imagesList.push({ src: img.src, caption: caption || `Figure ${idx + 1}` });
    });
  }

  // Open modal on click
  document.addEventListener('click', (e) => {
    const imgWrap = e.target.closest('.ss-img-wrap, .timeline-step-img');
    if (!imgWrap) return;

    const clickedImg = imgWrap.querySelector('img');
    if (!clickedImg || !clickedImg.src) return;

    refreshImagesList();
    const foundIdx = imagesList.findIndex(item => item.src === clickedImg.src);
    currentIndex = foundIdx !== -1 ? foundIdx : 0;

    updateModalImage(currentIndex);
    modal.classList.add('open');
  });

  const closeModal = () => modal.classList.remove('open');

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (prevBtn) prevBtn.addEventListener('click', (e) => { e.stopPropagation(); updateModalImage(currentIndex - 1); });
  if (nextBtn) nextBtn.addEventListener('click', (e) => { e.stopPropagation(); updateModalImage(currentIndex + 1); });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') updateModalImage(currentIndex - 1);
    if (e.key === 'ArrowRight') updateModalImage(currentIndex + 1);
  });
}"""

new_zoom = """/* ─────────────────────────────────────────
   12. CLICK TO ZOOM LIGHTBOX MODAL
──────────────────────────────────────────── */
function initZoomModal() {
  const modal = document.getElementById('zoom-modal');
  if (!modal) return;

  const modalImg = modal.querySelector('.modal-img');
  const modalCap = modal.querySelector('.modal-caption');
  const closeBtn = modal.querySelector('.modal-close');

  const closeModal = () => {
    modal.classList.remove('open');
    document.body.style.overflow = '';
    if (modalImg) modalImg.src = '';
  };

  const openModal = (src, caption) => {
    if (!src) return;
    if (modalImg) modalImg.src = src;
    if (modalCap) modalCap.textContent = caption || 'Screenshot Preview';
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  // Click any screenshot / image wrapper to zoom
  document.addEventListener('click', (e) => {
    const target = e.target;
    // Don't intercept clicks inside the open modal or on interactive controls
    if (target.closest('#zoom-modal') || target.closest('button') || target.closest('a')) return;

    const imgWrap = target.closest('.step-img-wrap, .ss-img-wrap, .proof-card, .step-card');
    let clickedImg = null;

    if (target.tagName === 'IMG') {
      clickedImg = target;
    } else if (imgWrap) {
      clickedImg = imgWrap.querySelector('img');
    }

    if (clickedImg && clickedImg.src && !clickedImg.closest('#zoom-modal')) {
      e.preventDefault();
      e.stopPropagation();
      const title = (imgWrap ? imgWrap.getAttribute('data-title') : null) || clickedImg.getAttribute('alt') || 'Screenshot Preview';
      openModal(clickedImg.src, title);
    }
  });

  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.classList.contains('modal-content') || e.target.classList.contains('modal-overlay')) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;
    if (e.key === 'Escape') closeModal();
  });
}"""

# Normalize \r\n for replacement
text_norm = text.replace('\r\n', '\n')
old_zoom_norm = old_zoom.replace('\r\n', '\n')
new_zoom_norm = new_zoom.replace('\r\n', '\n')

assert old_zoom_norm in text_norm, "old_zoom not found in script.js!"
text_norm = text_norm.replace(old_zoom_norm, new_zoom_norm)

# 2. Remove the old duplicate ssModal code
dup_marker = "  // 4. Modal Zoom for Step Screenshots and Proof Cards"
dup_pos = text_norm.find(dup_marker)
if dup_pos != -1:
    end_marker = "/* ─────────────────────────────────────────\n   GLOBAL ACTIONS: COPY, DOWNLOAD, PROFILE"
    end_pos = text_norm.find(end_marker, dup_pos)
    if end_pos != -1:
        text_norm = text_norm[:dup_pos] + text_norm[end_pos:]
        print("Removed duplicate ssModal code!")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text_norm)

print("script.js updated successfully!")

