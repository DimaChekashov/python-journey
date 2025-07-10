import { ReactNode, useState } from "react";
import AuthContext from "./AuthContext";

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const login = () => {};

  const logout = () => {};

  const register = () => {};

  const checkAuth = () => {};

  return (
    <AuthContext.Provider
      value={{ user, isLoading, login, logout, register, checkAuth }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
