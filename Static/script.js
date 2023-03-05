const toTop = document.querySelector(".to-top");

window.addEventListener("scroll", () => {
    if (window.pageYOffset > 100) {
        toTop.classList.add("active");
    }
    else {
        toTop.classList.remove("active");
    }
} )

// Dark/Light Mode 
var modeSwitch = document.getElementById('SwitchCheck');

if (localStorage.getItem('theme') == 'dark') {
    setDarkMode()

    if (modeSwitch.checked) {
        localStorage.setItem('SwitchCheck', true)
    }
}

function setDarkMode() {
    let isDark = document.body.classList.toggle('darkmode');

    if (isDark) {
        setDarkMode.checked = true;
        localStorage.setItem('theme', 'dark');
        modeSwitch.setAttribute('checked', 'checked');
    }
    else {
        setDarkMode.checked = false
        localStorage.removeItem('theme', 'dark');
    }
}

modeSwitch.addEventListener("click", setDarkMode)