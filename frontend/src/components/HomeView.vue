<style scoped>
.addmargin {
  margin-top: 0.625em;
  margin-bottom: 0.625em;
}

.home {
  background-color: #383c44;
}
</style>

<!--
<template>
  <article>
    <section v-for="(n, index) in pageOffset" :key="index">
      <img :src="'https://picsum.photos/400/400?image='+index" alt="">
      <p>
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
        sed diam nonumy eirmod tempor invidunt ut labore et dolore 
        magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
        et justo duo dolores et ea rebum.
      </p>
    </section>
    <footer>
      <div ref="infinitescrolltrigger" id="scoll-trigger"></div>
      <div class="circle-loader" v-if="showloader"></div>
    </footer>
  </article>
</template>
-->

<template>
  <div class="searchView">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/materia/bootstrap.min.css"
      integrity="sha384-B4morbeopVCSpzeC1c4nyV0d0cqvlSAfyXVfrPJa25im5p+yEN/YmhlgQP/OyMZD"
      crossorigin="anonymous"
    />
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="http://localhost:8080/">FitFam</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarColor02"
          aria-controls="navbarColor02"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarColor02">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <a class="nav-link active" href="/">Global</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/groups">Groups</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/profile">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/search">Search</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/login">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <p></p>
    <!--Template from Site-->
    <div class="card mb-3">
      <h3 class="card-header text-left">Profile Nickname</h3>
      <div class="card-body">
        <h5 class="card-title">Special title treatment</h5>
        <h6 class="card-subtitle text-muted">Support card subtitle</h6>
      </div>
      <div class="card-body">
        <p class="card-text">
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </p>
      </div>
      <div class="card-footer text-muted">2 days ago</div>
    </div>
    <!--Template from Site end-->
    <p></p>
    <p>{{ backend }}</p>
  </div>
</template>
<!--
<script>
  export default {
    data: () => {
      return {
        currentPage: 1,
        maxPerPage: 2,
        totalResults: 100,
        showloader: false
      }
    },
    computed: {
      pageCount() {
        return Math.ceil(this.totalResults/this.maxPerPage);
      },
      pageOffset() {
        return this.maxPerPage * this.currentPage;
      }
    },
    methods: {
      scrollTrigger() {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if(entry.intersectionRatio > 0 && this.currentPage < this.pageCount) {
              this.showloader = true;
              setTimeout(() => {
                this.currentPage += 1;
                this.showloader = false;
              }, 2000); // simulate Ajax-Call ;-)
            }
          });
        });

        observer.observe(this.$refs.infinitescrolltrigger);
      }
    },
    mounted() {
      this.scrollTrigger();
    }
  }
</script>
-->
<script>
import axios from "axios";

export default {
  data() {
    return {
      backend: "",
    };
  },
  methods: {
    getStats() {
      const path = "http://127.0.0.1:5000/home";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getStats();
  },
};
</script>
<!--
<style lang="scss" scoped>
  article {
    margin: 0 auto;
    width: 400px;

    section {
      width: 400px;
      margin-bottom: 20px;
      border-radius: 10px;
      background-color: #efefef;
      color: #04525A;
      overflow: hidden;

      p {
        margin: 0;
        padding: 10px 20px;
      }
    }

    footer {
      position: relative;
      width: 400px;
      height: 100px;

      #scroll-trigger {
        height: 50px;
      }

      .circle-loader {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 5px solid rgba(255, 255, 255, .2);
        border-top: 5px solid #fff;
        animation: animate 1.5s infinite linear;
      }
    }
  }

  @keyframes animate {
    0% {
      transform: translate(-50%,-50%) rotate(0deg);
    }
    100% {
      transform: translate(-50%,-50%) rotate(360deg);
    }
  }
</style>

-->
