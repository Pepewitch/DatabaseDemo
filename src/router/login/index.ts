import { Router } from 'express';
import passport from '../../passport';

const router = Router();

router.get('/', (req, res) => {
  return res.status(200).send(`
  <form action="/login" method="POST">
  <input name="username" placeholder="username" autocomplete="off">
  <input name="password" placeholder="password" autocomplete="off">
  <button type="submit">Submit</button>
  </form>
  <br>
  `);
});

router.get('/user', (req, res) => {
  return res.status(200).send({ user: req.user, session: req.session });
});

router.post(
  '/',
  passport.authenticate('local', { failureRedirect: '/login' }),
  (req, res) => {
    return res.redirect('/login/user');
  },
);

export default router;
