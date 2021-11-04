<template>
  <div>
    <form>
      <md-card>
        <md-card-header :data-background-color="dataBackgroundColor">
          <h4 class="title">Predict Your Course Program</h4>
          <p class="category">Please fill up all the fields and click submit</p>
        </md-card-header>
        <form @submit.prevent="validatePredictProgram()">
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-small-size-100 md-size-33">
                <md-field>
                  <label>GWA:</label>
                  <md-input v-model="gwa" type="number" required></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-33">

                <!-- <md-field required>
                  <label>Strand</label>
                  <md-select v-model="strand">
                    <md-option value="1">TVL</md-option>
                    <md-option value="2">ABM</md-option>
                    <md-option value="3">GAS</md-option>
                    <md-option value="4">STEM</md-option>
                    <md-option value="5">HUMSS</md-option>
                  </md-select>
                </md-field> -->
              <br>
              Strand:
              <br>
              <br>
              <md-radio v-model="strand" :value="1">TVL</md-radio>
              <md-radio v-model="strand" :value="2">ABM</md-radio>
              <md-radio v-model="strand" :value="3">GAS</md-radio>
              <md-radio v-model="strand" :value="4">STEM</md-radio>
              <md-radio v-model="strand" :value="5">HUMSS</md-radio>


              </div>
              <div class="md-layout-item md-small-size-100 md-size-33">
                <md-field>
                  <label>Admission Score</label>
                  <md-input
                    v-model="admissionScore"
                    type="number"
                    required
                  ></md-input>
                </md-field>
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
          Your Recommended program is: {{ recommendedProgram }}
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
  name: "PredictProgramForm",
  props: {
    dataBackgroundColor: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      gwa: null,
      strand: 1,
      admissionScore: null,

      replied: false,
      recommendedProgram: "",

      fireSnackbar: false,
      messageSnackbar: ""
    };
  },
  methods: {
    async validatePredictProgram() {
      this.fireSnackbar = true;
      this.messageSnackbar = "Loading...";
      var axios = require("axios");
      var FormData = require("form-data");
      var data = new FormData();
      data.append("gwa", this.gwa);
      data.append("strand", this.strand);
      data.append("admissionScore", this.admissionScore);

      var config = {
        method: "post",
        url: "http://localhost:5000/recommend-program",
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
        })
        .catch((error) => {
          console.log(error);
          this.replied = true;
          this.fireSnackbar = true;
          this.messageSnackbar = "There is an error attempting to predict your program";
        });
    },
  },
};
</script>
<style></style>
