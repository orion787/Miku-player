const audio = document.querySelector('.audio')
const playPauseBtn = document.querySelector('.play-pause-btn')
const prevBtn = document.querySelector('.prev-btn')
const nextBtn = document.querySelector('.next-btn')
const autoplayBtn = document.querySelector('.autoplay-btn')
const progressBar = document.querySelector('.progress-bar')
const volumeBar = document.querySelector('.volume-bar')
const playPauseIcon = playPauseBtn.querySelector('i')
const modal = document.querySelector('.modal')
const modalOpen = document.querySelector('.fa-ellipsis-h')
const modalClose = document.querySelector('.modal__close')
const autoplayText = document.querySelector('.player__text')

let isAutoplay = false
let currentTimeout

playPauseBtn.addEventListener('click', () => {
	if (audio.paused || audio.ended) {
		audio.play()
	} else {
		audio.pause()
	}
})

audio.addEventListener('play', () => {
	playPauseIcon.classList.remove('fa-play')
	playPauseIcon.classList.add('fa-pause')
})

audio.addEventListener('pause', () => {
	playPauseIcon.classList.remove('fa-pause')
	playPauseIcon.classList.add('fa-play')
})

audio.addEventListener('timeupdate', () => {
	progressBar.value = (audio.currentTime / audio.duration) * 100
})

audio.addEventListener('ended', () => {
	if (isAutoplay) {
		audio.play() // Повторно проигрывает трек, если включен автоплей
	}
})

progressBar.addEventListener('input', () => {
	audio.currentTime = (progressBar.value / 100) * audio.duration
})

volumeBar.addEventListener('input', () => {
	audio.volume = volumeBar.value / 100
})

autoplayBtn.addEventListener('click', () => {
	isAutoplay = !isAutoplay
	autoplayBtn.classList.toggle('active')

	// Очищаем текущий таймаут, если он есть
	if (currentTimeout) {
		clearTimeout(currentTimeout)
	}

	// Изменение цвета кнопки в зависимости от состояния
	if (isAutoplay) {
		autoplayText.textContent = 'Повтор трека включен!'
	} else {
		autoplayText.textContent = 'Повтор трека выключен!'
	}

	autoplayText.classList.add('player__text_active')

	// Устанавливаем новый таймаут и сохраняем его в переменную
	currentTimeout = setTimeout(() => {
		autoplayText.classList.remove('player__text_active')
	}, 3000)
})

modalOpen.addEventListener('click', () => {
	modal.classList.add('modal_active')
})

modalClose.addEventListener('click', () => {
	modal.classList.remove('modal_active')
})





function getSongIdFromUrl() {
    const pathArray = window.location.pathname.split('/');
    return pathArray[3]; 
}

prevBtn.addEventListener('click', () => {
	let songId = getSongIdFromUrl();
    window.location.pathname = `/audio/song/${songId}/previous/`;
})

nextBtn.addEventListener('click', () => {
	let songId = getSongIdFromUrl();
    window.location.pathname = `/audio/song/${songId}/next/`;
})




