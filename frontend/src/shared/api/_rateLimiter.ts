import { NextApiRequest, NextApiResponse } from "next";
import { RateLimiterMemory } from "rate-limiter-flexible";

const rateLimiter = new RateLimiterMemory({
  points: 50, // 10 запросов
  duration: 1, // за 1 секунду
});

export const checkRateLimit = async (
  req: NextApiRequest,
  res: NextApiResponse
) => {
  try {
    const ip = req.headers["x-forwarded-for"] || req.socket.remoteAddress;
    await rateLimiter.consume(ip as string);
    return true;
  } catch (err) {
    res.status(429).json({ error: "Too Many Requests" });
    return false;
  }
};
