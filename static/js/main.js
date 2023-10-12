/*=============== SWIPER JS ===============*/
let swiperCards = new Swiper(".card__content", {
  loop: true,
  spaceBetween: 32,
  grabCursor: true,

  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
    600: {
      slidesPerView: 2,
    },
    968: {
      slidesPerView: 3,
    },
  },
});
/*===============Reviews JS===============*/
let reviews = [];

function displayReviews() {
    const reviewsContainer = document.getElementById('reviews');
    reviewsContainer.innerHTML = '';

    reviews.forEach(review => {
        const reviewDiv = document.createElement('div');
        reviewDiv.className = 'review';
        reviewDiv.innerHTML = `
            <h3>${review.title}</h3>
            <p><strong>Rating:</strong> ${review.rating}</p>
            <p>${review.comment}</p>
            <hr>
        `;
        reviewsContainer.appendChild(reviewDiv);
    });
}

function addReview() {
    const title = prompt('Enter review title:');
    const rating = parseFloat(prompt('Enter rating (1-5):'));
    const comment = prompt('Enter your review:');

    if (title && !isNaN(rating) && rating >= 1 && rating <= 5 && comment) {
        const review = { title, rating, comment };
        reviews.push(review);
        displayReviews();
    } else {
        alert('Invalid input. Please try again.');
    }
}

// Initial reviews for demonstration
reviews.push({ title: 'Great Product', rating: 5, comment: 'I love this product!' });
reviews.push({ title: 'Could be Better', rating: 3, comment: 'Not bad, but could use improvements.' });

displayReviews();


// 컨텐츠 불러오기

fetch("http://127.0.0.1:8000/contents/movie/")
  .then((response) => response.json())
  .then((data) => console.log(data));

fetch("http://127.0.0.1:8000/contents/music/")
  .then((response) => response.json())
  .then((data) => console.log(data));  

fetch("http://127.0.0.1:8000/contents/game/")
  .then((response) => response.json())
  .then((data) => console.log(data)); 