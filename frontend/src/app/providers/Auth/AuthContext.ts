import { createContext } from "react";

interface AuthContextType {
  user: string;
  isLoading: boolean;
  login: () => void;
  logout: () => void;
  register: () => void;
  checkAuth: () => void;
}

const AuthContext = createContext<AuthContextType>({
  user: "",
  isLoading: false,
  login: () => {},
  logout: () => {},
  register: () => {},
  checkAuth: () => {},
});

export default AuthContext;
