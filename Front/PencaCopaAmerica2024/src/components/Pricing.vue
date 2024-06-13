<template>
    <button @click="showIndex" class="back-button">
        <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
    </button>
    <div class="container">
        <div class="left-side">
            <div class="card">
                <div class="card-line"></div>
                <div class="buttons"></div>
            </div>
            <div class="post">
                <div class="post-line"></div>
                <div class="screen">
                    <div class="dollar">$</div>
                </div>
                <div class="numbers"></div>
                <div class="numbers-line2"></div>
            </div>
        </div>
        <div class="right-side">
            <div class="new">
                <ul>
                    <li>Itaú - Ionas Josponis</li>
                    <li>CA 3652270</li>
                    <li>Moneda: UYU</li>
                </ul>
            </div>

            <svg viewBox="0 0 451.846 451.847" height="512" width="512" xmlns="http://www.w3.org/2000/svg"
                class="arrow">
                <path fill="#cfcfcf" data-old_color="#000000" class="active-path" data-original="#000000"
                    d="M345.441 248.292L151.154 442.573c-12.359 12.365-32.397 12.365-44.75 0-12.354-12.354-12.354-32.391 0-44.744L278.318 225.92 106.409 54.017c-12.354-12.359-12.354-32.394 0-44.748 12.354-12.359 32.391-12.359 44.75 0l194.287 194.284c6.177 6.18 9.262 14.271 9.262 22.366 0 8.099-3.091 16.196-9.267 22.373z">
                </path>
            </svg>

        </div>
    </div>
</template>

<script>
/* eslint-disable vue/multi-word-component-names */
export default {
    name: 'Pricing',
    methods: {
        showIndex() {
            this.$router.push('/index')
        }
    }

}
</script>

<style scoped>
.button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #1abc9c;
    color: white;
    cursor: pointer;
    margin: 10px;
}

.button:hover {
    background-color: #003c30;
}

.back-button img {
    width: 24px;
    height: 24px;
}

.container {
    background-color: #ffffff;
    display: flex;
    width: 460px;
    height: 120px;
    position: relative;
    border-radius: 6px;
    transition: 0.3s ease-in-out;
}

.container:hover {
    transform: scale(1.03);
    width: 220px;
}

.container:hover .left-side {
    width: 100%;
}

.left-side {
    background-color: #ff6201;
    width: 130px;
    height: 120px;
    border-radius: 4px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: 0.3s;
    flex-shrink: 0;
    overflow: hidden;
}

.right-side {
    width: calc(100% - 130px);
    display: flex;
    align-items: center;
    overflow: hidden;
    cursor: pointer;
    justify-content: space-between;
    white-space: nowrap;
    transition: 0.3s;
}

.right-side:hover {
    background-color: #f9f7f9;
}

.arrow {
    width: 20px;
    height: 20px;
    margin-right: 20px;
}

.new {
    font-size: 23px;
    font-family: "Lexend Deca", sans-serif;
    margin-left: 20px;
    color: black;
}

.card {
    width: 70px;
    height: 46px;
    background-color: #ffffff;
    border-radius: 6px;
    position: absolute;
    display: flex;
    z-index: 10;
    flex-direction: column;
    align-items: center;
    -webkit-box-shadow: 9px 9px 9px -2px #ff6201;
    -moz-box-shadow: 9px 9px 9px -2px #ff6201;
    -webkit-box-shadow: 9px 9px 9px -2px #ff6201;
}

.card-line {
    width: 65px;
    height: 13px;
    background-color: #ff6201;
    border-radius: 2px;
    margin-top: 7px;
}

@media only screen and (max-width: 480px) {
    .container {
        transform: scale(0.7);
    }

    .container:hover {
        transform: scale(0.74);
    }

    .new {
        font-size: 18px;
    }
}

.buttons {
    width: 8px;
    height: 8px;
    background-color: #ff6201;
    box-shadow: 0 -10px 0 0 #ff6201, 0 10px 0 0 #ff6201;
    border-radius: 50%;
    margin-top: 5px;
    transform: rotate(90deg);
    margin: 10px 0 0 -30px;
}

.container:hover .card {
    animation: slide-top 1.2s cubic-bezier(0.645, 0.045, 0.355, 1) both;
}

.container:hover .post {
    animation: slide-post 1s cubic-bezier(0.165, 0.84, 0.44, 1) both;
}

@keyframes slide-top {
    0% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }

    50% {
        -webkit-transform: translateY(-70px) rotate(90deg);
        transform: translateY(-70px) rotate(90deg);
    }

    60% {
        -webkit-transform: translateY(-70px) rotate(90deg);
        transform: translateY(-70px) rotate(90deg);
    }

    100% {
        -webkit-transform: translateY(-8px) rotate(90deg);
        transform: translateY(-8px) rotate(90deg);
    }
}

.post {
    width: 63px;
    height: 75px;
    background-color: #dddde0;
    position: absolute;
    z-index: 11;
    bottom: 10px;
    top: 120px;
    border-radius: 6px;
    overflow: hidden;
}

.post-line {
    width: 47px;
    height: 9px;
    background-color: #545354;
    position: absolute;
    border-radius: 0px 0px 3px 3px;
    right: 8px;
    top: 8px;
}

.post-line:before {
    content: "";
    position: absolute;
    width: 47px;
    height: 9px;
    background-color: #757375;
    top: -8px;
}

.screen {
    width: 47px;
    height: 23px;
    background-color: #ffffff;
    position: absolute;
    top: 22px;
    right: 8px;
    border-radius: 3px;
}

.numbers {
    width: 12px;
    height: 12px;
    background-color: #838183;
    box-shadow: 0 -18px 0 0 #838183, 0 18px 0 0 #838183;
    border-radius: 2px;
    position: absolute;
    transform: rotate(90deg);
    left: 25px;
    top: 52px;
}

.numbers-line2 {
    width: 12px;
    height: 12px;
    background-color: #aaa9ab;
    box-shadow: 0 -18px 0 0 #aaa9ab, 0 18px 0 0 #aaa9ab;
    border-radius: 2px;
    position: absolute;
    transform: rotate(90deg);
    left: 25px;
    top: 68px;
}

@keyframes slide-post {
    50% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }

    100% {
        -webkit-transform: translateY(-70px);
        transform: translateY(-70px);
    }
}

.dollar {
    position: absolute;
    font-size: 16px;
    font-family: "Lexend Deca", sans-serif;
    width: 100%;
    left: 0;
    top: 0;
    color: #4b953b;
    text-align: center;
}

.container:hover .dollar {
    animation: fade-in-fwd 0.3s 1s backwards;
}

@keyframes fade-in-fwd {
    0% {
        opacity: 0;
        transform: translateY(-5px);
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

li {
    list-style: none;
}


.back-button {
    position: fixed;
    top: 10px;
    left: 10px;
    padding: 5px;
    background-color: transparent;
    border: none;
}

.back-button img {
    width: 24px;
    height: 24px;
}
</style>