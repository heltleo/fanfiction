<template>
    <div class="flex flex-wrap">
        <Loading v-if="loading" />
        <div class="w-full sm:w-1/2 md:w-1/4 mb-4">

              <p>Vous êtes connecter en tant que {{ user.username }}.</p>
              <ul class="list-reset">
                 <li> <router-link v-if="$route.name !== 'ListUserFanfic'" tag="button" :to="{name: 'ListUserFanfic'}">
                      Voir mes fanfictions
                  </router-link></li>
                  <li><router-link v-if="$route.name !== 'NewFanfic'" tag="button" :to="{name: 'NewFanfic'}">
                      Ecrire une fanfiction
                  </router-link></li>

                  <li><router-link v-if="$route.name !== 'ChangePassword'" tag="button" :to="{ name: 'ChangePassword' }">
                      Changer le mot de passe
                  </router-link></li>

                  <li><button class="text-red hover:text-red-darker" @click.prevent="disableAccount">
                    Supprimer le compte
                </button></li>
              </ul>
          </div>
          <div class="w-full sm:w-1/2 md:w-3/4 mb-4">

              <router-view />

          </div>
    </div>
</template>

<script>
export default {
    name: 'Dashboard',
    data(){
        return{
            error: null,
            user: [],
            loading: false,
        }
    },
    async created () {
        this.loading = true
        try {
            this.user = await this.$fetch('user')
        } catch (e) {
            this.error = e
        }
        this.loading = false
    },
    methods: {
        async disableAccount () {
            let message = confirm("Après la suppression, votre compte sera désactivé et aucune opération ne pourra être effectuer. Supprimer le compte ?")

            if (message === true) {
                const result = await this.$fetch('disable-account')
                if (result.status === 'ok') {
                    this.$state.user = null
                    if (this.$route.matched.some(m => m.meta.private)) {
                        this.$router.push({ name: 'List' })
                    }
                }
            }

        }
    }
}
</script>

<style scoped>
</style>
