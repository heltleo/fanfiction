<template>
    <div class="w-full max-w-md">

        <Form
        class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
        title="Nouvelle histoire"
        :operation="operation"
        :valid="valid">
        <div class="flex flex-wrap -mx-3 mb-6">
            <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
              <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="category">
                Catégorie
              </label>
              <div class="relative">
                  <select class="block appearance-none w-full bg-white border border-grey-light hover:border-grey px-4 py-2 pr-8 rounded shadow" id="category" name="category" v-model="category">
                      <option value="">Sélectionner</option>
                      <option v-for="(option, index) of dataCategories" v-bind:value="option.id">{{ option.name }}</option>
                  </select>
                  <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                      <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                  </div>
              </div>
            </div>
            <div class="w-full md:w-1/2 px-3">
              <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="subcategory">
                  Sous - Catégories
              </label>
              <div class="relative">
                  <select :disabled="category.length == 0" class="block appearance-none w-full bg-white border border-grey-light hover:border-grey px-4 py-2 pr-8 rounded shadow" id="subcategory" name="subcategory" v-model="subcategory">
                      <option value="">Sélectionner</option>
                      <option v-for="(option, index) of dataSubCategories" v-if="option.category === category" v-bind:value="option.id">{{ option.name }}</option>
                  </select>
                  <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                      <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                  </div>
              </div>
            </div>
          </div>
            <div class="mb-4">
                <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="title">
                  Titre de l'histoire
                </label>
                <Input
                    name="title"
                    v-model="title"
                    placeholder="Titre de l'histoire"
                    maxlength="255"
                    required />
            </div>
            <div class="mb-4">
                <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="synopsis">
                  Synopsis
                </label>
                <Input
                    type="textarea"
                    name="synopsis"
                    v-model="synopsis"
                    placeholder="Synopsis"
                    maxlength="1000"
                    rows="4" />
            </div>
            <div class="mb-4">
                <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="credits">
                  Crédits
                </label>
                <Input
                    type="textarea"
                    name="credits"
                    v-model="credits"
                    placeholder="Crédits"
                    maxlength="350" />
            </div>
            <div class="mb-6">
                <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="description">
                  Description de l'histoire
                </label>
                <Input
                    type="textarea"
                    name="description"
                    v-model="description"
                    placeholder="Description"
                    maxlength="1000"
                    rows="4" />
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                    <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="classement">
                      Classement
                    </label>
                    <div class="relative">
                        <select class="block appearance-none w-full bg-white border border-grey-light hover:border-grey px-4 py-2 pr-8 rounded shadow" id="classement" name="classement" v-model="classement" v-if="loadingClassement">
                            <option value="">Sélectionner</option>
                            <option v-for="(option, index) in dataClassement[0]['classement']" v-bind:value="option[0]">{{ option[1] }}</option>
                        </select>
                        <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
                <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                    <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="genres">
                      Genres
                    </label>
                    <div class="relative">
                        <label v-if="loadingGenres" v-for="(genre, index) in dataGenres">
                            <input type="checkbox" v-bind:value="genre[0]" v-model="genres">
                            {{ genre[1] }}<br/>
                        </label>
                    </div>
                </div>
                <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
                    <label class="block tracking-wide text-grey-darker text-xs font-bold mb-2" for="status">
                      Status
                    </label>
                    <div class="relative">
                        <select class="block appearance-none w-full bg-white border border-grey-light hover:border-grey px-4 py-2 pr-8 rounded shadow" id="status" name="status" v-model="status" v-if="loadingStatus">
                            <option value="">Sélectionner</option>
                            <option v-for="(option, index) in dataStatus[0]['status']"  v-bind:value="option[0]">{{ option[1] }}</option>
                        </select>
                        <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/></svg>
                        </div>
                    </div>
                </div>
            </div>
            <template slot="actions">
                <router-link
                    tag="button"
                    :to="{name: 'ListUserFanfic'}"
                    class="secondary inline-block align-baseline font-bold text-sm text-blue hover:text-blue-darker">
                    Retour à la liste des fanfictions
                </router-link>
                <button
                    type="submit"
                    class="bg-blue hover:bg-blue-dark text-white font-bold py-2 px-4 rounded"
                    :disabled="!valid">
                    Créer une histoire
                </button>
            </template>
        </Form>
    </div>
</template>

<script>
import PersistantData from '../mixins/PersistantData'

export default {
    name: 'NewFanfic',
    mixins: [
        PersistantData('NewFanfic', [
            'title',
            'description',
            'synopsis',
            'credits',
            'author',
            'classement',
            'status',
            'category',
            'subcategory',
        ]),
    ],
    data(){
        return{
            error: null,
            dataClassement: [],
            dataStatus: [],
            dataCategories: [],
            dataSubCategories: [],
            dataGenres: {},
            title: '',
            description: '',
            synopsis: '',
            credits: '',
            author: '',
            genres: [],
            classement: '',
            status: '',
            category: '',
            subcategory: '',
            loadingClassement: false,
            loadingGenres: false,
            loadingStatus: false,
        }
    },
    computed: {
        valid () {
            return !!this.title && !!this.category && !!this.subcategory && !!this.status && !!this.genres && !!this.classement
        }
    },

    mounted () {
        this.getClassement ()
        this.getCategories ()
        this.getSubcategories ()
        this.getStatus ()
        this.getGenres ()
    },
    methods: {
        async operation () {
            const result = await this.$fetch('fanfics', {
                method: 'POST',
                body: JSON.stringify({
                    title: this.title,
                    description: this.description,
                    synopsis: this.synopsis,
                    credits: this.credits,
                    author: this.$state.user.id,
                    genres: this.genres,
                    classement: this.classement,
                    status: this.status,
                    category: this.category,
                    subcategory: this.subcategory,
                }),
            })
            this.title = this.description = this.synopsis = this.credits = this.author = this.genres = this.classement = this.status = this.category = this.subcategory = ''
        },
        async getGenres() {
            this.dataGenres = await this.$fetch('fanfics/genres')
            this.loadingGenres = true
            this.dataGenres = this.dataGenres[0]['genres']
        },
        async getClassement() {
            this.dataClassement = await this.$fetch('fanfics/classement')
            this.loadingClassement = true
        },
        async getStatus() {
            this.dataStatus = await this.$fetch('fanfics/status')
            this.loadingStatus = true
        },
        async getCategories() {
            this.dataCategories = await this.$fetch('category')
        },
        async getSubcategories() {
            this.dataSubCategories = await this.$fetch('subcategory')
        },
    },
}
</script>

<style scoped>
.w-full {
    margin: 0 auto;
}
</style>
