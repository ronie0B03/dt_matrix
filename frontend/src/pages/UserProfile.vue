<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <PredictProgramForm data-background-color="green"> </PredictProgramForm>
      </div>
      <!-- <div class="md-layout-item md-medium-size-100 md-size-33">
        <UserCard> </UserCard>
      </div> -->
    </div>
  </div>
</template>

<script>
import { PredictProgramForm, /** UserCard **/ } from "@/pages";

export default {
  components: {
    PredictProgramForm,
    // UserCard,
  },
};
</script>
