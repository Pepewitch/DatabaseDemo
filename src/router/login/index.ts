import { Router } from 'express';
import passport from '../../passport';
import { facebook_scope } from '../../passport/strategy/facebook';
import { google_scope } from '../../passport/strategy/google';

const router = Router();

router.get('/', (req, res) => {
  console.log({ user: req.user });
  return res.status(200).send(`
  ${
    req.user
      ? `
      <form action="/login/logout" method="POST">
      <button type="submit">Logout</button>
      </form>`
      : `<form action="/login" method="POST">
    <input name="username" placeholder="username" autocomplete="off">
    <input name="password" placeholder="password" autocomplete="off">
    <button type="submit">Submit</button>
    </form>
    <br>
    <form action="/login/facebook" method="GET">
    <button type="submit">Login with facebook</button>
    </form>
    <form action="/login/google" method="GET">
    <button type="submit">Login with google</button>
    </form>`
  }
  `);
});

router.post('/logout', (req, res) => {
  if (req.user) {
    req.logOut();
  }
  return res.sendStatus(200);
});

router.get('/user', (req, res) => {
  return res.status(200).send({ user: req.user, session: req.session });
});

router.get(
  '/facebook',
  passport.authenticate('facebook', { scope: facebook_scope, session: false }),
);

router.get(
  '/facebook/callback',
  passport.authenticate('facebook', {
    failureRedirect: '/login',
    session: false,
  }),
  (req, res) => {
    console.log(req.user);
    return res.redirect('/login/user');
  },
);

router.get(
  '/google',
  passport.authenticate('google', { scope: google_scope, session: false }),
);

router.get(
  '/google/callback',
  passport.authenticate('google', {
    failureRedirect: '/login',
    session: false,
  }),
  (req, res) => {
    console.log(req.user);
    return res.redirect('/login/user');
  },
);

router.get(
  '/facebook/callback',
  passport.authenticate('facebook', {
    failureRedirect: '/login',
    session: false,
  }),
  (req, res) => {
    console.log(req.user);
    return res.redirect('/login/user');
  },
);

router.post(
  '/',
  passport.authenticate('local', { failureRedirect: '/login' }),
  (req, res) => {
    return res.redirect('/login/user');
  },
);

export default router;
