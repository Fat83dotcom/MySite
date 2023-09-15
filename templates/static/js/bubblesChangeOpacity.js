window.addEventListener('load', ()=>{
    let element = document.getElementById('bubbles')
    element.style.display = 'flex'
    setTimeout(()=>{
        element.style.opacity = '1'
    }, 2000)
})