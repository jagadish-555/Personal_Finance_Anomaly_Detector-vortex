import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';

export default function Hero() {
    return (
        <section className="pt-48 pb-32 md:pt-56 md:pb-40 px-6 max-w-[1400px] mx-auto text-center flex flex-col items-center justify-center min-h-[85vh] relative overflow-hidden">
            {/* Background Glows */}
            <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-indigo-500/10 rounded-full blur-[120px] pointer-events-none" />
            <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[120px] pointer-events-none" />

            <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                className="max-w-[1000px] mx-auto relative z-10"
            >
                <h1 className="text-[56px] leading-[1.05] md:text-[80px] lg:text-[100px] font-bold text-white tracking-[-0.04em] mb-8">
                    Detect unusual spending before it becomes a problem.
                </h1>
            </motion.div>

            <motion.p
                className="text-xl md:text-[22px] text-gray-400 max-w-[640px] mx-auto leading-[1.6] mb-12 font-medium relative z-10"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            >
                AI-powered transaction monitoring that alerts you to suspicious, unexpected, or abnormal financial behavior instantly.
            </motion.p>

            <motion.div
                className="flex flex-col sm:flex-row gap-4 items-center justify-center w-full sm:w-auto relative z-10"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            >
                <Link to="/dashboard" className="w-full sm:w-auto bg-indigo-600 text-white px-8 py-4 rounded-full text-[17px] font-semibold hover:bg-indigo-500 transition-colors inline-block shadow-[0_0_30px_rgba(99,102,241,0.3)] hover:shadow-[0_0_40px_rgba(99,102,241,0.5)]">
                    Get Started
                </Link>
                <a href="#how-it-works" className="w-full sm:w-auto bg-white/5 backdrop-blur-md text-white px-8 py-4 rounded-full text-[17px] font-semibold border border-white/10 hover:bg-white/10 transition-colors inline-block">
                    Book a Demo
                </a>
            </motion.div>
        </section>
    );
}
