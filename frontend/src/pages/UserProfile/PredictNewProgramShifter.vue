<template>
  <div>
    <form>
      <md-card>
        <md-card-header :data-background-color="dataBackgroundColor">
          <h4 class="title">Program recommender for shifter</h4>
          <p class="category">
            Please fill up all the fields and click proceed
          </p>
        </md-card-header>
        <form @submit.prevent="validatePredictShiftProgram()">
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-small-size-100 md-size-33">
                <md-field>
                  <label>Age:</label>
                  <md-input v-model="age" type="number" required></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-33">
                Strand:
                <br />
                <md-radio v-model="strand" :value="0">STEM</md-radio>
                <md-radio v-model="strand" :value="1">TVL</md-radio>
                <md-radio v-model="strand" :value="2">GAS</md-radio>
                <md-radio v-model="strand" :value="3">HUMSS</md-radio>
                <md-radio v-model="strand" :value="4">ABM</md-radio>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-33">
                <md-field>
                  <label>Admission Test Score</label>
                  <md-input
                    v-model="admissionScore"
                    type="number"
                    required
                  ></md-input>
                </md-field>
              </div>

              <div class="md-layout-item md-small-size-100 md-size-33">
                Status Regular / Irregular:
                <br />
                <md-radio v-model="status" :value="0">Regular</md-radio>
                <md-radio v-model="status" :value="1">Irregular</md-radio>
                <md-radio v-model="status" :value="2">Drop</md-radio>
              </div>

              <div class="md-layout-item md-small-size-100 md-size-33">
                Current GWA / Semester Grade:
                <br />
                <md-radio v-model="gradeGWA" :value="0">Less than 2</md-radio>
                <md-radio v-model="gradeGWA" :value="1"
                  >Greater than or Equal 2</md-radio
                >
              </div>

              <div class="md-layout-item md-small-size-100 md-size-33">
                Gender
                <br />
                <md-radio v-model="gender" :value="0">Male</md-radio>
                <md-radio v-model="gender" :value="1">Female</md-radio>
              </div>

              <div class="md-layout-item md-small-size-100 md-size-33">
                Current Program:
                <br />
                <md-radio v-model="currentProgram" :value="0">BSIT</md-radio>
                <md-radio v-model="currentProgram" :value="1"
                  >BIT-FOODS</md-radio
                >
                <md-radio v-model="currentProgram" :value="2"
                  >BIT-AUTO</md-radio
                >
                <md-radio v-model="currentProgram" :value="3"
                  >BIT-DRAFT</md-radio
                >
                <md-radio v-model="currentProgram" :value="4"
                  >BIT-ELECTRICAL</md-radio
                >
                <md-radio v-model="currentProgram" :value="5"
                  >BSED-ENG</md-radio
                >
                <md-radio v-model="currentProgram" :value="6">BPED</md-radio>
                <md-radio v-model="currentProgram" :value="7"
                  >BSED-GEN ED</md-radio
                >
                <md-radio v-model="currentProgram" :value="8">BSBA</md-radio>
                <md-radio v-model="currentProgram" :value="9"
                  >BS-ENTREP</md-radio
                >
                <md-radio v-model="currentProgram" :value="10">HRM</md-radio>
                <md-radio v-model="currentProgram" :value="11"
                  >COMP-ENGR</md-radio
                >
                <md-radio v-model="currentProgram" :value="12">BSIE</md-radio>
                <md-radio v-model="currentProgram" :value="13">BEED</md-radio>
              </div>

              <div class="md-layout-item md-size-100 text-right">
                <md-button class="md-raised md-success" type="submit"
                  >Proceed</md-button
                >
              </div>
            </div>
          </md-card-content>
        </form>
      </md-card>
    </form>

    <div v-if="replied">
      <md-card>
        <md-card-content>
          Your recommended program for shifting is:
          {{ recommendedProgramTitle }}
        </md-card-content>

        <!-- <md-card-actions>
          <md-button>Action</md-button>
          <md-button>Action</md-button>
        </md-card-actions> -->
      </md-card>
    </div>
    <!-- Program recommender for shifter -->
    <form>
      <md-card>
        <md-card-header :data-background-color="dataBackgroundColor">
          <h4 class="title">
            Check which subjects the students are having hard time
          </h4>
          <p class="category">
            Please fill up all the fields and click proceed
          </p>
        </md-card-header>
        <form @submit.prevent="validateSubjectsHardTime()">
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-small-size-100 md-size-100">
                Program / Course:
                <br />
                <md-radio v-model="forProgram" :value="0">BSIT</md-radio>
                <md-radio v-model="forProgram" :value="1">BEED</md-radio>
                <md-radio v-model="forProgram" :value="2">FOODS</md-radio>
                <md-radio v-model="forProgram" :value="3">BAFM</md-radio>
                <md-radio v-model="forProgram" :value="4">COE</md-radio>
              </div>

              <div class="md-layout-item md-size-100 text-right">
                <md-button class="md-raised md-success" type="submit"
                  >Proceed</md-button
                >
              </div>
            </div>
          </md-card-content>
        </form>
      </md-card>
    </form>

    <div v-if="repliedOnSubjects">
      <md-card>
        <md-card-content>
          Their subjects that they are having hard time are the following:
          {{ recommendedProgram }}
        </md-card-content>

        <!-- <md-card-actions>
          <md-button>Action</md-button>
          <md-button>Action</md-button>
        </md-card-actions> -->
      </md-card>
    </div>

    <md-snackbar
      :md-position="'center'"
      :md-duration="5000"
      :md-active.sync="fireSnackbar"
      md-persistent
    >
      <span>{{ messageSnackbar }}</span>
      <md-button class="md-warning md-dense" @click="fireSnackbar = false">
        <label style="color: black">Dismiss</label>
      </md-button>
    </md-snackbar>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "PredictNewProgramShifter.vue",
  props: {
    dataBackgroundColor: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      age: 0,
      gender: 0,
      strand: 1,
      admissionScore: 0,
      status: 0,
      gradeGWA: 0,
      currentProgram: 0,

      forProgram: 0,

      replied: false,
      repliedOnSubjects: false,
      recommendedProgram: "",
      recommendedProgramTitle: "",

      fireSnackbar: false,
      messageSnackbar: "",
    };
  },
  methods: {
    async validatePredictShiftProgram() {
      this.fireSnackbar = true;
      this.messageSnackbar = "Loading...";
      var axios = require("axios");
      var FormData = require("form-data");
      var data = new FormData();
      data.append("age", this.age);
      data.append("strand", this.strand);
      data.append("admissionScore", this.admissionScore);
      data.append("status", this.status);
      data.append("gradeGWA", this.gradeGWA);
      data.append("gender", this.gender);
      data.append("currentProgram", this.currentProgram);

      var config = {
        method: "post",
        url: "http://localhost:5000/recommend-shift-program",
        headers: {},
        data: data,
      };

      await axios(config)
        .then((response) => {
          console.log(JSON.stringify(response.data));
          this.replied = true;
          this.recommendedProgram = response.data.program;
          console.log(JSON.stringify(response.data.program));
          this.fireSnackbar = false;

          //Condition for the program
          if (this.recommendedProgram === 0) {
            this.recommendedProgramTitle = "BSIT";
          } else if (this.recommendedProgram === 1) {
            this.recommendedProgramTitle = "BIT-FOODS";
          } else if (this.recommendedProgram === 2) {
            this.recommendedProgramTitle = "BIT-AUTO";
          } else if (this.recommendedProgram === 3) {
            this.recommendedProgramTitle = "BIT-DRAFT";
          } else if (this.recommendedProgram === 4) {
            this.recommendedProgramTitle = "BIT-ELECTRICAL";
          } else if (this.recommendedProgram === 5) {
            this.recommendedProgramTitle = "BSED-ENG";
          } else if (this.recommendedProgram === 6) {
            this.recommendedProgramTitle = "BPED";
          } else if (this.recommendedProgram === 7) {
            this.recommendedProgramTitle = "BSED-GEN ED";
          } else if (this.recommendedProgram === 8) {
            this.recommendedProgramTitle = "BSBA";
          } else if (this.recommendedProgram === 9) {
            this.recommendedProgramTitle = "BS-ENTREP";
          } else if (this.recommendedProgram === 10) {
            this.recommendedProgramTitle = "HRM";
          } else if (this.recommendedProgram === 12) {
            this.recommendedProgramTitle = "COMP ENGR";
          } else if (this.recommendedProgram === 13) {
            this.recommendedProgramTitle = "BSIE";
          } else if (this.recommendedProgram === 14) {
            this.recommendedProgramTitle = "BEED";
          }
        })
        .catch((error) => {
          console.log(error);
          this.replied = true;
          this.fireSnackbar = true;
          this.messageSnackbar =
            "There is an error attempting to predict your program";
        });
    },

    async validateSubjectsHardTime() {
      this.fireSnackbar = true;
      this.messageSnackbar = "Loading...";
      var axios = require("axios");
      var FormData = require("form-data");
      var data = new FormData();
      data.append("program", this.forProgram);

      var config = {
        method: "post",
        url: "http://localhost:5000/check-subject-hard-time",
        headers: {},
        data: data,
      };

      await axios(config)
        .then((response) => {
          console.log(JSON.stringify(response.data));
          this.repliedOnSubjects = true;
          this.recommendedProgram = response.data.subjects
          console.log(this.recommendedProgram)
          console.log(JSON.stringify(response.data.subjects));
          this.fireSnackbar = false;
        })
        .catch((error) => {
          console.log(error);
          this.repliedOnSubjects = true;
          this.fireSnackbar = true;
          this.messageSnackbar =
            "There is an error attempting to predict your program";
        });
    },
  },
};
</script>
<style>
.md-size-33 {
  margin-bottom: 2% !important;
}
</style>
