(function () {
  function setupWhatsAppFloat() {
    const root = document.querySelector("[data-wa-float]");
    if (!root) return;

    const btn = root.querySelector("[data-wa-toggle]");
    const closeBtn = root.querySelector("[data-wa-close]");
    const panel = root.querySelector("[data-wa-panel]");

    function open() {
      root.classList.add("is-open");
      btn.setAttribute("aria-expanded", "true");
    }

    function close() {
      root.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    }

    function toggle() {
      if (root.classList.contains("is-open")) close();
      else open();
    }

    btn?.addEventListener("click", toggle);
    closeBtn?.addEventListener("click", close);

    // Fecha clicando fora
    document.addEventListener("click", (e) => {
      if (!root.classList.contains("is-open")) return;
      if (root.contains(e.target)) return;
      close();
    });

    // Fecha com ESC
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") close();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupWhatsAppFloat);
  } else {
    setupWhatsAppFloat();
  }
})();
