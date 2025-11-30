#!/bin/bash

# WALK THIS WAY - Pages to TXT Conversion Script
# Created: October 9, 2024
# Purpose: Convert all .pages files to .txt with consistent naming

echo "🚀 WALK THIS WAY - PAGES CONVERSION SCRIPT"
echo "=========================================="
echo ""

# Set the script directory as working directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"
echo ""

# Create backup directory for original .pages files
BACKUP_DIR="Archive_Pre_Reorg/Pages_Originals"
mkdir -p "$BACKUP_DIR"
echo "📦 Created backup directory: $BACKUP_DIR"
echo ""

# Counter for processed files
CONVERTED_COUNT=0
ERROR_COUNT=0

echo "🔍 Searching for .pages files..."
echo ""

# Find all .pages files recursively
find . -name "*.pages" -type f | while read -r pages_file; do
    echo "📄 Processing: $pages_file"
    
    # Get directory and filename without extension
    dir_name=$(dirname "$pages_file")
    base_name=$(basename "$pages_file" .pages)
    
    # Create output directory if it doesn't exist
    output_dir="$dir_name"
    
    # Determine output filename based on pattern
    if [[ $base_name =~ ^[Cc]hapter[[:space:]]*([0-9]+) ]]; then
        # Matches "Chapter 4" or "chapter 4"
        chapter_num=$(printf "%02d" "${BASH_REMATCH[1]}")
        output_name="Ch_${chapter_num}_Working.txt"
    elif [[ $base_name =~ ^[Cc]h[[:space:]]*([0-9]+) ]]; then
        # Matches "Ch 4" or "ch 4"
        chapter_num=$(printf "%02d" "${BASH_REMATCH[1]}")
        output_name="Ch_${chapter_num}_Working.txt"
    elif [[ $base_name =~ ^[Cc]h_([0-9]+) ]]; then
        # Matches "Ch_4" or "ch_4"
        chapter_num=$(printf "%02d" "${BASH_REMATCH[1]}")
        output_name="Ch_${chapter_num}_Working.txt"
    else
        # Default naming
        output_name="${base_name}.txt"
    fi
    
    output_path="$output_dir/$output_name"
    
    echo "   📝 Output: $output_path"
    
    # Try to convert using textutil (built into macOS)
    if command -v textutil &> /dev/null; then
        echo "   🔄 Converting with textutil..."
        if textutil -convert txt "$pages_file" -output "$output_path" 2>/dev/null; then
            echo "   ✅ SUCCESS: Converted to $output_path"
            ((CONVERTED_COUNT++))
        else
            echo "   ❌ ERROR: textutil failed for $pages_file"
            ((ERROR_COUNT++))
        fi
    else
        echo "   ❌ ERROR: textutil not available"
        ((ERROR_COUNT++))
    fi
    
    # Move original .pages file to backup
    backup_path="$BACKUP_DIR/$(basename "$pages_file")"
    mv "$pages_file" "$backup_path"
    echo "   📦 Backed up original to: $backup_path"
    echo ""
done

echo "🎉 CONVERSION COMPLETE!"
echo "======================="
echo "✅ Files converted: $CONVERTED_COUNT"
echo "❌ Errors: $ERROR_COUNT"
echo "📦 Originals backed up to: $BACKUP_DIR"
echo ""

# If any files were converted, add them to Git
if [ $CONVERTED_COUNT -gt 0 ]; then
    echo "📚 Adding converted files to Git..."
    git add .
    git commit -m "Convert Pages files to TXT with consistent naming"
    echo "✅ Files committed to Git"
    echo ""
fi

echo "🚀 NEXT STEPS:"
echo "1. Check the converted .txt files"
echo "2. Review naming conventions"
echo "3. Begin systematic revision!"
echo ""
echo "💡 TIP: Use 'git log' to see all changes"
echo "💡 TIP: Use 'git status' to see current state"
echo ""

# Show current directory structure
echo "📁 CURRENT STRUCTURE:"
find Chapters -name "*.txt" | sort
echo ""

echo "🎯 Ready to write!"
