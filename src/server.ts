import app from './app';
import Controller from './controllers';

app.listen(process.env.PORT || 3000, () => {
  console.log('Start server at port :', process.env.PORT || 3000);
  Controller.testConnection();
});
