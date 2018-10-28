import Controller from '..';
import { User } from '../../entity/User';
import { AsyncErrorHandler } from '../../decorators/error-handler';

interface UserOption extends UserInfo {
  id?: number;
}

interface UserInfo {
  firstName?: string;
  lastName?: string;
  age?: number;
}

export default class UserController {
  @AsyncErrorHandler()
  public static async getUsers(options?: UserOption) {
    const connection = await Controller.getConnection();
    const users = await connection.manager.find(User, { where: options });
    return users;
  }

  @AsyncErrorHandler()
  public static async addUser(options: UserInfo) {
    const connection = await Controller.getConnection();
    const user = new User();
    Object.assign(user, options);
    await connection.manager.save(user);
  }
}
