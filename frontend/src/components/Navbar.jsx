import React from 'react';

export default function Navbar() {
    return (
        <nav className="fixed top-0 w-full z-50 bg-[#09090b]/80 backdrop-blur-xl border-b border-white/5">
            <div className="max-w-[1400px] mx-auto px-6 h-20 flex items-center justify-between">

                {/* Logo Left */}
                <div className="flex-shrink-0 flex items-center gap-2">
                    <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-[0_0_15px_rgba(99,102,241,0.5)]">
                        <span className="text-white font-bold text-sm tracking-tighter">V</span>
                    </div>
                    <span className="font-bold text-xl tracking-tight text-white">Vortex</span>
                </div>

                {/* Centered Nav Links */}
                <div className="hidden md:flex flex-1 justify-center space-x-10">
                    <a href="#features" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">Features</a>
