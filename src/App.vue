<template>
    <div id="app" class="container mx-auto">
        <app-header v-bind:title="title"></app-header>
        <transition name="fade" mode="out-in">
            <router-view />
        </transition>
        <app-footer v-bind:title="title"></app-footer>
        <transition appear name="slideFromBottom">
            <div class="cookie bottom" v-if="isOpen">
                <div class="cookie__content">
                    Ce site utilise des cookies pour vous assurer la meilleure expérience sur notre site.
                </div>
                <div class="cookie__buttons">
                    <div class="cookie__button" @click="accept">J'ai compris</div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import * as Cookie from 'tiny-cookie'

import '@/assets/styles/main.css'

import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
    name: 'App',
    components: {
        'app-header': Header,
        'app-footer': Footer,
    },
    data () {
        return {
            title: 'Fanfiction',
            isOpen: false,
            supportsLocalStorage: true
        };
    },
    created () {
        // Check for availability of localStorage
        try {
            const test = '__vue-cookielaw-check-localStorage'
            window.localStorage.setItem(test, test)
            window.localStorage.removeItem(test)
        } catch (e) {
            console.error('Local storage is not supported, falling back to cookie use')
            this.supportsLocalStorage = false
        }
        if (!this.getVisited() === true) {
            this.isOpen = true
        }
    },
    methods: {
        setVisited () {
            if (this.supportsLocalStorage) {
                localStorage.setItem('cookie:accepted', true)
            } else {
                Cookie.set('cookie:accepted', true)
            }
        },
        getVisited () {
            if (this.supportsLocalStorage) {
                return localStorage.getItem('cookie:accepted')
            } else {
                return Cookie.get('cookie:accepted')
            }
        },
        accept () {
            this.setVisited()
            this.isOpen = false
            this.$emit('accept')
        }
    }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 15px;
}

.cookie {
    position: fixed;
    overflow: hidden;
    box-sizing: border-box;
    z-index: 9999;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    flex-direction: row;
    background: #4dc0b5;
    color: #fff;
    padding: 1.250em;
}

.cookie > * {
    align-self: center;
}

.cookie.bottom {
    bottom: 0;
    left: 0;
    right: 0;
}

.cookie__buttons {
    margin-top: 5px;
    display: flex;
    flex-direction: column;
}

.cookie__button {
    background: #fff;
    padding: 0.625em 3.125em;
    color: #4dc0b5;
    border-radius: 20px;
    cursor: pointer;
}
.cookie__button:hover {
    background: #38a89d;
    color: #fff;
}
.slideFromBottom-enter, .slideFromBottom-leave-to {
    transform: translate(0px, 12.500em);
}
.slideFromBottom-enter-to, .slideFromBottom-leave {
    transform: translate(0px, 0px);
}
.slideFromBottom-enter-active,
.slideFromBottom-leave-active {
    transition: transform .4s ease-in;
}

.fade-enter-active, .fade-leave-active {
    transition: opacity .1s;
}

.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
}

</style>
