import passport from 'passport';
import UserController from '../controllers/User/UserController';
import { User } from '../entity/User';
import local from './local';

passport.serializeUser((user: User, done) => {
  done(null, user.username);
});

passport.deserializeUser(async (username: string, done) => {
  try {
    const user = await UserController.getUser(username);
    done(null, user);
  } catch (err) {
    done(err, null);
  }
});

passport.use(local);

export default passport;
