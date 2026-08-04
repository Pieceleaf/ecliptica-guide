/* 公共脚本：修复 Chrome 窗口 resize 后底部白屏（渲染层未重绘 bug）
   ——resize 时强制触发 relayout/重绘，替代"手动拖窗口" */
(function () {
  // 记录最后一次视口尺寸
  let lastW = window.innerWidth, lastH = window.innerHeight;
  function forceRepaint() {
    // 微调根元素 min-height 触发 relayout（立即还原，视觉无变化）
    var html = document.documentElement;
    var prev = html.style.minHeight;
    html.style.minHeight = (window.innerHeight - 1) + 'px';
    // 双 rAF 确保合成层更新
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        html.style.minHeight = prev;
        // 额外触发一次 GPU 合成：切换一个不透明度的 transform
        var b = document.body;
        b.style.transform = 'translateZ(0)';
        requestAnimationFrame(function () { b.style.transform = ''; });
      });
    });
  }
  window.addEventListener('resize', function () {
    var w = window.innerWidth, h = window.innerHeight;
    if (w !== lastW || h !== lastH) {
      lastW = w; lastH = h;
      // 延迟到浏览器完成窗口尺寸更新后触发
      setTimeout(forceRepaint, 50);
    }
  });
  // 页面加载时也强制一次（覆盖"加载时就处于竖屏"的情况）
  if (document.readyState === 'complete') forceRepaint();
  else window.addEventListener('load', forceRepaint);
})();

/* Phase 3: 全站底部导航、键盘交互与弹层语义 */
(function () {
  const page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  const pageKey = page.replace(/\.html$/, '').replace(/[^a-z0-9_-]/g, '') || 'index';
  document.body.classList.add('site-page', `site-page-${pageKey}`);
  document.body.dataset.sitePage = page;

  const nav = document.querySelector('.bottom-nav');
  if (nav) {
    const items = [
      ['index.html', '🏠', '首页'],
      ['upgrades.html', '📖', '图鉴'],
      ['builds.html', '🛠️', 'Build'],
      ['simulator.html', '🎯', '模拟器']
    ];
    const moreActive = ['classes.html', 'stats.html', 'changelog.html'].includes(page);
    nav.innerHTML = items.map(([href, icon, label]) => {
      const active = href === page;
      return `<a href="${href}" class="${active ? 'active' : ''}" ${active ? 'aria-current="page"' : ''}><span class="bn-ico" aria-hidden="true">${icon}</span><span>${label}</span></a>`;
    }).join('') + `<button type="button" class="bottom-more${moreActive ? ' more-active' : ''}" id="bottomMoreBtn" aria-haspopup="dialog" aria-controls="siteMoreDrawer"><span class="bn-ico" aria-hidden="true">•••</span><span>更多</span></button>`;
  }

  let moreDrawer = document.getElementById('siteMoreDrawer');
  if (!moreDrawer) {
    document.body.insertAdjacentHTML('beforeend', `
      <div class="detail-modal site-more-drawer" id="siteMoreDrawer" role="dialog" aria-modal="true" aria-labelledby="siteMoreDrawerTitle">
        <div class="dm-box">
          <div class="dm-handle"></div>
          <div class="site-more-head"><h3 id="siteMoreDrawerTitle">更多页面</h3><button type="button" class="dm-cancel" data-site-more-close aria-label="关闭更多页面">关闭</button></div>
          <div class="site-more-list">
            <a href="classes.html" data-more-link="classes.html"><span aria-hidden="true">⚔️</span><span>职业</span></a>
            <a href="stats.html" data-more-link="stats.html"><span aria-hidden="true">📊</span><span>属性上限</span></a>
            <a href="changelog.html" data-more-link="changelog.html"><span aria-hidden="true">📜</span><span>版本日志</span></a>
          </div>
        </div>
      </div>`);
    moreDrawer = document.getElementById('siteMoreDrawer');
  }
  const closeMore = () => { moreDrawer.classList.remove('show'); document.body.classList.remove('modal-open'); };
  const openMore = () => { moreDrawer.classList.add('show'); document.body.classList.add('modal-open'); };
  document.getElementById('bottomMoreBtn')?.addEventListener('click', openMore);
  moreDrawer.querySelector('[data-site-more-close]')?.addEventListener('click', closeMore);
  moreDrawer.addEventListener('click', e => { if (e.target === moreDrawer) closeMore(); });
  moreDrawer.querySelectorAll('[data-more-link]').forEach(link => {
    if (link.dataset.moreLink === page) { link.classList.add('active'); link.setAttribute('aria-current', 'page'); }
  });

  const interactive = '.class-card, .build-opt, .prio-item, .skill-icon, .boss-card, .enemy-card';
  function enhanceInteractive() {
    document.querySelectorAll(interactive).forEach(el => {
      if (el.tabIndex >= 0) return;   // 已增强过，跳过（减少高频渲染开销）
      el.tabIndex = 0;
      if (!el.hasAttribute('role')) el.setAttribute('role', 'button');
    });
    document.querySelectorAll('.pick-row').forEach(el => {
      if (el.tabIndex >= 0) return;
      el.tabIndex = 0;
      if (!el.hasAttribute('role')) el.setAttribute('role', 'button');
    });
  }
  enhanceInteractive();
  new MutationObserver(enhanceInteractive).observe(document.body, { childList: true, subtree: true });
  document.addEventListener('keydown', e => {
    const el = e.target.closest(interactive);
    if (el && (e.key === 'Enter' || e.key === ' ')) {
      e.preventDefault();
      el.click();
      return;
    }
    const row = e.target.closest('.pick-row[data-id]');
    if (row && e.key === 'Enter' && typeof window.openDetail === 'function') {
      e.preventDefault();
      window.openDetail(row.dataset.id, row.closest('#smPicker') !== null);
    }
  });
  document.addEventListener('focusin', e => {
    const el = e.target.closest('.skill-icon, .pick-row');
    if (el) el.classList.add('keyboard-focus');
  });
  document.addEventListener('focusout', e => {
    const el = e.target.closest('.skill-icon, .pick-row');
    if (el && !el.contains(e.relatedTarget)) el.classList.remove('keyboard-focus');
  });
  const smClose = document.getElementById('smClose');
  if (smClose) {
    smClose.tabIndex = 0;
    smClose.setAttribute('role', 'button');
    smClose.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); smClose.click(); } });
  }

  const dialogLabels = {
    searchModal: '搜索技能', detailModal: '技能详情', artModal: '神器管理', statsModal: '当前属性',
    buildModal: '选择职业与 Build', saveModal: '保存自定义 Build', shareModal: '生成分享链接',
    moreDrawer: '更多操作', filterDrawer: '技能筛选', buildDrawer: 'Build 选择', siteMoreDrawer: '更多页面'
  };
  let dialogEnhancing = false;   // 防止 observer 回调内 DOM 写入触发自身（死循环）
  function enhanceDialogs() {
    if (dialogEnhancing) return;
    dialogEnhancing = true;
    try {
      document.querySelectorAll('.detail-modal, .search-modal').forEach(dialog => {
        if (dialog.getAttribute('aria-labelledby')) return;   // 已增强过，跳过
        const title = dialog.querySelector('h2, h3, [data-dialog-title], .sr-only') || (() => {
          const node = document.createElement('span');
          node.className = 'sr-only';
          node.textContent = dialogLabels[dialog.id] || '对话框';
          dialog.insertBefore(node, dialog.firstChild);
          return node;
        })();
        if (!title.id) title.id = `${dialog.id}-title`;
        dialog.setAttribute('role', 'dialog');
        dialog.setAttribute('aria-modal', 'true');
        dialog.setAttribute('aria-labelledby', title.id);
      });
    } finally {
      dialogEnhancing = false;
    }
  }
  enhanceDialogs();
  new MutationObserver(enhanceDialogs).observe(document.body, { childList: true, subtree: true });
})();
