// Seleciona o elemento que você quer animar
const element_title_1 = document.querySelector('.animated-eff-1');
const element_title_2 = document.querySelector('.animated-eff-2');
const element_title_3 = document.querySelector('.animated-eff-3');
const element_pic_1 = document.querySelector('.animated-pic-1');
const element_pic_2 = document.querySelector('.animated-pic-2');
const element_pic_3 = document.querySelector('.animated-pic-3');
const element_text_1 = document.querySelector('.animated-text-1');
const element_text_2 = document.querySelector('.animated-text-2');
const element_text_3 = document.querySelector('.animated-text-3');

// Configura as opções para o IntersectionObserver
const options = {
    root: null,
    rootMargin: '0px',
    threshold: 1 // Define quando a interseção será observada, aqui 0.5 significa que a metade do elemento precisa estar visível na tela
};
const options_2 = {
    root: null,
    rootMargin: '0px',
    threshold: 0.5 // Define quando a interseção será observada, aqui 0.5 significa que a metade do elemento precisa estar visível na tela
};

// Função callback para quando a interseção ocorrer
const callback_title_left = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Adiciona a classe CSS para ativar a animação
            entry.target.classList.add('animated-eff-end', 'anime-icons-index-left'); // Aqui 'fadeIn' é a classe de animação do Animate.css
            observer.unobserve(entry.target); // Para de observar o elemento depois de ativado
        }
    });
};

const callback_pics_down = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Adiciona a classe CSS para ativar a animação
            entry.target.classList.add('animated-eff-end', 'anime-icons-index-up'); // Aqui 'fadeIn' é a classe de animação do Animate.css
            observer.unobserve(entry.target); // Para de observar o elemento depois de ativado
        }
    });
};

const callback_text_right = (entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Adiciona a classe CSS para ativar a animação
            entry.target.classList.add('animated-eff-end', 'anime-icons-index-right'); // Aqui 'fadeIn' é a classe de animação do Animate.css
            observer.unobserve(entry.target); // Para de observar o elemento depois de ativado
        }
    });
};

// Cria o IntersectionObserver
const observer_title_1 = new IntersectionObserver(callback_title_left, options);
const observer_title_2 = new IntersectionObserver(callback_title_left, options);
const observer_title_3 = new IntersectionObserver(callback_title_left, options);
const observer_pic_1 = new IntersectionObserver(callback_pics_down, options_2);
const observer_pic_2 = new IntersectionObserver(callback_pics_down, options_2);
const observer_pic_3 = new IntersectionObserver(callback_pics_down, options_2);
const observer_text_1 = new IntersectionObserver(callback_text_right, options);
const observer_text_2 = new IntersectionObserver(callback_text_right, options);
const observer_text_3 = new IntersectionObserver(callback_text_right, options);

// Começa a observar o elemento
observer_title_1.observe(element_title_1);
observer_title_2.observe(element_title_2);
observer_title_3.observe(element_title_3);
observer_pic_1.observe(element_pic_1)
observer_pic_2.observe(element_pic_2)
observer_pic_3.observe(element_pic_3)
observer_text_1.observe(element_text_1)
observer_text_2.observe(element_text_2)
observer_text_3.observe(element_text_3)