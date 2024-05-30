
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
