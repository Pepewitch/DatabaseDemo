import { Router } from 'express';

const router = Router();

router.get('/ping', (req, res) => {
  return res.status(200).send({ message: 'pong' });
});

export default router;
