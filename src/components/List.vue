<template>
  <div>
  <Loading v-if="remoteDataBusy" />

    <div class="error bg-red-lightest border border-red-light text-red-dark px-4 py-3 rounded relative" v-if="hasRemoteErrors" role="alert">
        {{ errorFetch }}
    </div>

    <form class="align-center w-full max-w-sm">
        <div class="flex items-center py-2">
            <input class="appearance-none bg-transparent border-none w-full text-grey-darker mr-3 py-1 px-2 leading-tight" type="text" placeholder="Rechercher des fanfictions..." v-model="search_term" aria-label="Search">
            <button class="bg-teal hover:bg-teal-dark text-white font-bold py-2 px-4 rounded" @click.prevent="getSearchFanfics">Rechercher</button>
        </div>
  </form>

    <section>
        <ul class="flex flex-wrap list-reset -mx-2">
            <li class="md:w-1/3 sm:w-1/2 w-full px-2 relative overflow mb-4" v-for="(category, index) in categories" :key="category.id" v-if="categories && categories.length > 0 && index <= limitationList"><a href="#tsr" class="pointer" @click="sortByCategories(category.id)">
                <div v-if="category.logic_value !== ''" :style="{backgroundImage: 'url(' + require('./../assets/img/categories/'+ category.logic_value + '.jpg') + ')' }" :alt="category.name" :title="category.name" class="img-thumbnail border border-grey-light shadow"></div>
                <div v-else :style="{backgroundImage: 'url(' + require('./../assets/img/categories/empty.jpg') + ')' }" class="img-thumbnail border border-grey-light shadow"></div>
                <span class="caption">{{ category.name }}</span>
            </a></li>
        </ul>
        <div class="flex">
            <div @click="readMore(limitationList)" class="flex-1 mb-4 cursor-pointer bg-teal hover:bg-teal-dark text-center text-white font-bold py-2 px-4 rounded-full">Voir {{ limitationList == 2 ? 'plus': 'moins'}}</div>
        </div>

        <article class="flex flex-wrap -mx-2">
            <div id="tsr" class="mb-4 w-full px-2 md:w-1/2" v-for="fanfic of fanficList">
                <router-link class="no-underline" :to="{
                  name: 'Detail',
                  params: {
                    slug: fanfic.slug,
                    id: fanfic.id
                  },
                }">
                    <div class="border border-grey-light bg-white rounded p-4 flex flex-col justify-between leading-normal">
                        <div class="mb-8">
                            <p class="text-sm text-grey-dark flex items-center">
                            {{ fanfic.category }} / {{ fanfic.subcategory }}
                          </p>
                            <div class="text-black font-bold text-xl mb-2">{{ fanfic.title }}</div>
                            <p v-if="fanfic.synopsis" v-html="fanfic.synopsis" class="text-grey-darker text-base"></p>
                        </div>
                        <div class="flex items-center">
                            <div class="text-sm">
                                <p class="text-black leading-none">
                                    Auteur: <router-link :to="{ name: 'ShowUserFanfic', params: { username: fanfic.author, slug: fanfic.slug, id: fanfic.id } }" class="block mt-4 lg:inline-block lg:mt-0 text-teal hover:text-teal-darker">{{ fanfic.author }}</router-link>
                                </p>
                                <p class="text-grey-dark">Publié le : {{ fanfic.publish | date }}</p>
                                <p class="text-grey-dark">{{ fanfic.genres }} / {{ fanfic.classement }} / {{ fanfic.total_likes }} likes</p>
                            </div>
                        </div>
                    </div>
                    </router-link>
            </div>
        </article>

        <div v-if="empty">Pas encore de fanfictions dans cette catégorie.
            <router-link :to="{ name: 'Login' }" class="block mt-4 lg:inline-block lg:mt-0 text-teal hover:text-teal-darker">Créez la votre !</router-link>
        </div>

    </section>

  </div>
</template>

<script>
import RemoteData from '../mixins/RemoteData'

export default {
  name: 'List',
  mixins: [
      RemoteData({
          fanficList () {
              return 'fanfics/v1?category=&subcategory=&status=publié';
          },
          categories () {
              return 'category'
          }
      }),
  ],
  data () {
    return {
        errorFetch: 'Il y a un problème avec la requète.',
        search_term: '',
        categories: [],
        fanficList: [],
        empty: false,
        moreStr: 'Voir plus',
        limitationList: 2
        }
    },
    methods: {
      async getSearchFanfics () {

            try {
                this.fanficList = await this.$fetch(`fanfics/v1?category=&subcategory=&status=publié&search=${this.search_term}`)
            } catch (e) {
                this.errorFetch = e
            }
      },
      async sortByCategories (categoryId) {
          try {
              this.fanficList = await this.$fetch(`fanfics/v1?category=${categoryId}&subcategory=&status=publié`)
              if (this.fanficList.length === 0) {
                  this.empty = true
              } else {
                  this.empty = false
              }
          } catch (e) {
              this.errorFetch = e
          }
      },
      readMore (limitationList) {
          if (this.limitationList == this.categories.length) {
              this.limitationList = 2
          } else {
              this.limitationList = this.categories.length
          }
      }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.img-thumbnail {
    height: 250px;
    background-size: cover;
}

.caption {
    background: rgba(0, 0, 0, 0.5);
    color: #fff;
    display: table;
    position: absolute;
    float: left;
    text-transform: uppercase;
    bottom: 15%;
    padding: 5px;
}
</style>
