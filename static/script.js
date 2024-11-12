// Récupérer tous les éléments étoile
const stars = document.querySelectorAll('.star');
let selectedRating = 0;

// Fonction pour mettre à jour la sélection
function updateRating(rating) {
  stars.forEach(star => {
    star.classList.toggle('selected', star.dataset.value <= rating);
  });
  document.getElementById('rating-value').textContent = `Votre note : ${rating}`;
  selectedRating = rating;
}

// Événements de clic sur chaque étoile
stars.forEach(star => {
  star.addEventListener('click', () => {
    const rating = star.dataset.value;
    updateRating(rating);
    // Ici, vous pouvez envoyer la note à votre backend si nécessaire
    console.log(`La note sélectionnée est ${rating}`);
  });
});
