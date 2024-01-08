document.addEventListener('DOMContentLoaded', function () {
    bulmaCarousel.attach('#skin-carousel', {
        slidesToScroll: 1,
        slidesToShow: 1,
        initialSlide: 0,
        navigation: true,
        navigationKeys: true,
        pagination: true,
        loop: true,
        infinite: true,
        autoplay: true,
    })
});