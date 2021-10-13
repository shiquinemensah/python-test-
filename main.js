const openModalButtons = document.querySelector('[data-modal-target]')
const closeModalButtons = document.querySelector('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})


function openModal(modal) {
    if (modal == null ) return
    99
    modal.classList.add('active')
    overlay.classList.remove('active')
}