const request = require('supertest');

const buildApp = require('../../app');
const UserRepo = require('../../repos/user-repo');
const pool = require('../../pool');

const { randomBytes } = require('crypto');
const { default: migrate } = require('node-pg-migrate');
const format = require('pg-format');
const Context = require('../context');
let context;
beforeAll(async () => {
  context = await Context.build();
});
afterAll(() => {
  return context.close();
});
beforeEach(async () => { 
  await context.reset();
});

it('create a user', async () => {
  const startingCount = await UserRepo.count();
  expect(startingCount).toEqual(0);
  await request(buildApp())
    .post('/users')
    .send({ username: 'testuser', bio: 'test bio' })
    .expect(200);
  const finishCount = await UserRepo.count();
  expect(finishCount).toEqual(1);
});
