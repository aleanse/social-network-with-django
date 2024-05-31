
    document.addEventListener('DOMContentLoaded', () => {
    const bell = document.querySelector('.notification-bell');
    const sound = document.getElementById('notification-sound');
    bell.addEventListener('click', () => {
    if (bell.classList.contains('active')) {
        bell.classList.remove('active');
        sound.pause();
        sound.currentTime = 0;
    } else {
        bell.classList.add('active');
        sound.play();
    }
});
});


function likeButton(){
            let heart = document.querySelector('.heart');
            let likes = document.querySelector('.likes');
            if(heart.src.match("heart.png")){
                heart.src = "heart_red.png";
                likes.innerHTML = "5,490 likes";
            } else {
                heart.src = "heart.png";
                likes.innerHTML = "5,489 likes"
            }
        }
function toggleMenu() {
    var navLinks = document.getElementById("navLinks");
    navLinks.classList.toggle("active"); // Adiciona ou remove a classe 'active' para exibir ou esconder o menu
}
