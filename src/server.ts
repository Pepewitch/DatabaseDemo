import express from "express";
import { Model } from "./model/model";

const app = express();
app.get("/", (req, res) => {
  new Model();
  return res.status(200).send({ message: "Hello world" });
});
app.listen(80)