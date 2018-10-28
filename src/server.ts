import app from './app';
import UserController from './controllers/User/UserController';

UserController.getUsers();

app.listen(process.env.PORT || 3000);
