// SPA: une seule section visible à la fois
function showSection(id){
  // cacher toutes les sections
  document.querySelectorAll('.section').forEach(s=>{
    s.classList.remove('active');
    s.style.display='none';
  });
  // afficher la cible
  const tgt = document.querySelector(id);
  if(!tgt) return;
  tgt.style.display='block';
  setTimeout(()=>tgt.classList.add('active'), 20);
  window.scrollTo({top:0, behavior:'smooth'});
}

// au chargement: montrer seulement #accueil
document.addEventListener('DOMContentLoaded', ()=>{
  document.querySelectorAll('.section').forEach(s=>s.style.display='none');
  const home = document.querySelector('#accueil');
  if(home){ home.style.display='block'; setTimeout(()=>home.classList.add('active'), 20); }

  // navigation
  document.querySelectorAll('.nav-links a, .cta a, .top-actions a[href^="#"]').forEach(a=>{
    a.addEventListener('click', (e)=>{
      const href = a.getAttribute('href') || '';
      if(href.startsWith('#')){
        e.preventDefault();
        showSection(href);
      }
    });
  });
});
