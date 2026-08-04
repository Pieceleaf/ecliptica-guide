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
